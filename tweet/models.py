from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class tweet(models.Model): 
    name = models.CharField(max_length= 14)
    body = models.CharField(max_length= 140) 
    image = CloudinaryField('image')
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     