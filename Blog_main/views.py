from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Category,Blog,About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm # login html er authentication er jnno 
from django.contrib import auth # user data gulake entered dara er sathe match kranor jnno import kora hoise

def home(request):
    # return HttpResponse('Hello Mc')
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True,status = 'Published').order_by("updated_at")
    posts = Blog.objects.filter(is_featured = False, status = 'Published')
    about = About.objects.all()
    context = {
        # 'categories': categories, # jehetu context_processors.py te already daoa hoise tai ar alada vabe daoar drkr nau
        'featured_posts': featured_posts,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html',context)

def register(rqst):
    if rqst.method == 'POST':
        form = RegistrationForm(rqst.POST)
        if form.is_valid(): 
            form.save()
            return redirect('register')
        # else : print(form.errors)
    else:
        form = RegistrationForm()
        
    context = {
        'frm' : form,
    }
    return render(rqst,'register.html',context)

def login(rqst):
    if rqst.method == 'POST':
        form = AuthenticationForm(rqst,rqst.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username,password=password)
            if user is not None: auth.login(rqst, user)
            return redirect('home')
    form = AuthenticationForm()
    context={
        'frm':form,
    }
    return render(rqst,'login.html',context)

def logout(rqst):
    auth.logout(rqst)
    return redirect('home')