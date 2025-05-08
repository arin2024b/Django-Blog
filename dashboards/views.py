from django.shortcuts import  render,redirect,get_object_or_404

from blogs.models import Category,Blog
from .forms import CategoryForm,PostForm

# dashboard ta jate logged in user ei access krte pare tar jnno login_decorators er proyojn hbe
from django.contrib.auth.decorators import login_required

# login_required decorator use krle er vitor login_url dite hbe,, to dashboard er url ta jdi kno logged in chara 
#  kno user direct url likhe search kore tahole take direct login page a nia jabe

# Create your views here.
@login_required(login_url='login') # login page er name='login' chilo tai login url a login daoa hoise
def dashboard(rqst):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context ={
        'cat_count':category_count,
        'blg_count':blog_count,
    }
    return render(rqst,'dashboard/dashboard.html',context)

def categories(rqst):
    return render(rqst,'dashboard/categories.html')

def add_category(rqst):
    if rqst.method == 'POST':
        form = CategoryForm(rqst.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context={
        'form':form,
    }
    return render(rqst,'dashboard/add_category.html',context)

def edit_category(rqst,pk):
    category = get_object_or_404(Category,pk=pk)
    if rqst.method == 'POST':
        form = CategoryForm(rqst.POST , instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category) # intance er jnno edit form a oi category ta show krbe jeta edit krte chai
    context = {
        'form':form,
        'category':category, # ei category ta edit form a action er pk dite kaje lagbe
    }
    return render(rqst,'dashboard/edit_category.html',context)

def delete_category(rqst,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')
    
    
    
def posts(rqst):
    posts = Blog.objects.all()
    
    context={
        'posts':posts,
    }
    return render(rqst,'dashboard/posts.html',context)

def add_post(rqst):
    if rqst.method == 'POST':
        form = PostForm(rqst.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = PostForm()
    context={
        'form':form,
    }
    return render(rqst,'dashboard/add_post.html',context)

def edit_post(rqst,pk):
    post = get_object_or_404(Blog,pk=pk)
    if rqst.method == 'POST':
        form = PostForm(rqst.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = PostForm(instance=post)
    context ={
        'form':form,
        'post':post, # ei post ta edit form a action er pk dite kaje lagbe
        
    }
    return render(rqst,'dashboard/edit_post.html',context)

def delete_post(rqst,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')
