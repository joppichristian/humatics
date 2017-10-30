from django.shortcuts import render
from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializers,UserSerializer
from django.contrib.auth.models import User
from .permissions import IsAdminOrReadOnly


class ImageView(viewsets.ModelViewSet):
    queryset =  Image.objects.all()
    serializer_class = ImageSerializers
    permission_classes = (IsAdminOrReadOnly, )
    

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )