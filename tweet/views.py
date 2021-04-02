from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):  
    return render (request, 'index.html')  

def about(request):
    return render (request, 'about.html') 
    
def posttweet(request):
     
    return render (request, 'post-tweet.html') 

def index(request):   
    return render(request, 'picture/index.html')