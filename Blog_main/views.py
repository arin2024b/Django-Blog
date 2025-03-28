from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog,About

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