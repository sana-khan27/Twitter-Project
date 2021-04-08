from django.forms import ModelForm
from .models import TweetDB

# Create the form class.
class tweetForm(ModelForm):
    class Meta:
        model = TweetDB
        fields = ['name', 'body', 'image']