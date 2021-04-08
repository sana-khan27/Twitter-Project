from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from .forms import tweetForm
from .models import TweetDB
# Create your views here.

def add(request): 
    if request.method == 'POST':
        form = tweetForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else: 
            print(form.errors)
    return HttpResponseRedirect('/')
            
def home(request):
    ## This function gets all the tweet data
    tweets = TweetDB.objects.order_by('created_at').reverse().all() 
    
    ### Show these tweet 
    return render(request,'index.html',{'tweets':tweets}) ### sending from python to html , and we are using HTML class to see our vairable


def edit(request,tweet_id):  
    tweet = TweetDB.objects.get(id=tweet_id)
    if request.POST: 
        form=tweetForm(request.POST ,request.FILES,instance=tweet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else: 
            print(form.errors)
    form = tweetForm(instance = tweet)
    return render(request, 'edit.html',{'tweet':tweet,'form':form})

def delete(request,tweet_id):
    tweet = TweetDB.objects.get(id=tweet_id)
    tweet.delete()
    return HttpResponseRedirect('/')

