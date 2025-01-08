from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.blog import models
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def Login(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        password = request.POST.get('upassword')

        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/login')

    return render(request, "login.html")

def SignUp(request):
    if request.method =="POST":
        name = request.POST.get('uname')
        email= request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/login')
    return render(request, "signup.html")

@login_required(login_url='/login')
def Home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "home.html", context)


def SignOut(request):
    logout(request)
    return redirect('/login')


def MyPost(request):
    context = {
        'posts': Post.objects.filter(author= request.user)
    }
    return render(request, 'my_post.html', context)



@login_required(login_url='/login')
def NewPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    return render(request, "new_post.html")