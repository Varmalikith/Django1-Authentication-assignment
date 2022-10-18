from contextlib import _RedirectStream
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from login_form import settings
from django.core.mail import send_mail

def home(request):
    return render(request, "home_page.html")

def home1(request):
    return render(request, "index.html")

def home2(request):
    return render(request, "index1.html")

def signup(request): 

    if request.method == "POST":
        username=request.POST['username'] 
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        specialiazation=request.Post['specialiazation']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exists Please try another username")
            return redirect('home1')

        if User.objects.filter(email=email):
            messages.error(request,"email already taken")
            return redirect('home1')  
 
        if len(username)>10:
            messages.error(request,"username must be in 10 characters")

        if pass1 != pass2:
            messages.error(request,"password didn't match")

        if not username.isalnum():
            messages.error(request,"Username must be alpha numeric")
            return redirect('home1')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname              

        myuser.save()

        messages.success(request, "Your account has been Successfully Created" + myuser.first_name + " Doctor.")

       
    
    return render(request, "signup.html")

def signup1(request): 

    if request.method == "POST":
        username=request.POST['username'] 
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        

        if User.objects.filter(username=username):
            messages.error(request,"Username already exists Please try another username")
            return redirect('home2')

        if User.objects.filter(email=email):
            messages.error(request,"email already taken")
            return redirect('home2')  
 
        if len(username)>10:
            messages.error(request,"username must be in 10 characters")

        if pass1 != pass2:
            messages.error(request,"password didn't match")

        if not username.isalnum():
            messages.error(request,"Username must be alpha numeric")
            return redirect('home2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname              

        myuser.save()

        messages.success(request, "Your account has been Successfully Created " + myuser.first_name)

       
    
    return render(request, "signup1.html") 

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, 'index.html',{'fname':fname})
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('home')
    
    return render(request, "signin.html")

def signin1(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, 'index1.html',{'fname':fname})
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('home')
    
    return render(request, "signin1.html") 
    

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')       