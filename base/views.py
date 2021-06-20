from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import Url

# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    print('registration started')
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        obj = User.objects.create_user(username=username,email=email,first_name=first_name,password=password)
        return render(request,"home.html",{'message':'registration successful'})
    
def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        obj = authenticate(username=username,password=password)
        if obj is not None:
            auth.login(request,obj)
            return render(request,"home.html",{'message':'login successful'})

def create(request):
    if request.method=="POST":
        longurl = request.POST["longurl"]
        shorturl = request.POST["shorturl"]
        Url.objects.create(longurl=longurl,shorturl=shorturl,user=request.user,count=0)
        message = 'shorturl created successfully'
        return render(request,"home.html",{'message':message})

def bitly(request,short):
    obj = Url.objects.filter(shorturl=short)
    if len(obj)==0:
        message = 'No URL Exist'
        return render(request,"home.html",{'message':message})
    else:
        return HttpResponseRedirect(obj[0].longurl)