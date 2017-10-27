from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('api.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
] 