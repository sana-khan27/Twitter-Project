from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class TweetDB(models.Model):
    name = models.CharField(max_length=14)
    body = models.CharField(max_length=140)
    image = CloudinaryField('image', blank=True)
    likes = models.PositiveIntegerField(
        'like', default=0, blank=True, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
