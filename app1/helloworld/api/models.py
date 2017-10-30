from django.db import models

class Image (models.Model):
    name = models.CharField(max_length=40);
    path = models.CharField(max_length=500);
    urls = models.BooleanField(default=False);