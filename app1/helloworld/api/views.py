from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Image
from .serializers import ImageSerializers,UserSerializer
from django.contrib.auth.models import User
from .permissions import IsAdminOrReadOnly, AllowAny
from django.core.files.images import ImageFile
from django.core.exceptions import ValidationError
from rest_framework.decorators import detail_route
from rest_framework.response import Response
import logging, os, urllib
logger = logging.getLogger(__name__)


class ImageView(viewsets.ModelViewSet):

    queryset = Image.objects.all()
    serializer_class = ImageSerializers
    permission_classes = (AllowAny, )
    print("PRE POST")
    def create(self, request):
        print("POST")
        # Validate the incoming input (provided through post parameters)    
        name = request.data.get('name')
        pic  = request.data.get('pic')            
        pic_urls = request.data.get('urls')
        print("DEBUG" + pic_urls)
        if not pic_urls:
            print("DEBUG CASE 1")
            pic = request.data.get('pic')
            obj = Image(name = name, pic = pic)
            obj.save()
            return Response({"message": "Immagine caricata!"}, status.HTTP_200_OK)
        else:
            print("DEBUG CASE 2")
            try:
                out_path = os.path.join(os.path.dirname(__file__), 'img.jpg')
                urllib.request.urlretrieve(pic_urls, out_path)
                out_file = open(out_path, 'rb+')
                F = ImageFile(out_file)
                F.name = os.path.basename(pic_urls)
                print("DEBUG F" + F.name)
            except:
                raise ValidationError("Impossibile scaricare correttamente l'immmagine dal web.")
            obj = Image(name = name, urls = pic_urls, pic = F)
            obj.save()
            return Response({"message": "Immagine caricata!"}, status.HTTP_200_OK)

        

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )