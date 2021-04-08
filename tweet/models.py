from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class TweetDB(models.Model): 
    name = models.CharField(max_length= 14)
    body = models.CharField(max_length= 140) 
    image = CloudinaryField('image',blank=True)
    like_count = models.IntegerField(default=0,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     