from django.shortcuts import  render,redirect,get_object_or_404

from blogs.models import Category,Blog
from .forms import CategoryForm,PostForm

# autometic slug generate krar jnno slugify import krte hbe
from django.template.defaultfilters import slugify  # eta post er add/edit operation a slug er autometically generate er jnno

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
        form = PostForm(rqst.POST,rqst.FILES) # file type data (image) naoar jnno request.FILES use krte hbe but age form a enctype="multipart/form-data" ta dite hbe
        if form.is_valid():
             # form theke slug and author er option baad daoa hoise,, models.py a slug er blank=True er jnno na likhleo first post add krle error dibena but 2nd post add krte gele error suru hbe and 
            # author akebarei na dile error dibe tai author take  autometically manage krte hbe,jei user logged in thakbe sei jate by default oi post er author hoye jay
            post = form.save(commit=False) # temporarily saving the form
            post.author = rqst.user # ekhne by default user oi post er author hoy hbe
            post.save() # finally the form will be saved..  and eta save krar karone nicha post.id ta paoa jabe nahole error through krto
            
            # autometic slug generate krar jnno (title theke):
            title = form.cleaned_data['title']
            post.slug = slugify(title) +'-'+str(post.id)
            post.save()
            
            return redirect('posts')
        else: return redirect('404') #print(form.errors)
    form = PostForm()
    context={
        'form':form,
    }
    return render(rqst,'dashboard/add_post.html',context)

def edit_post(rqst,pk):
    post = get_object_or_404(Blog,pk=pk)
    if rqst.method == 'POST':
        form = PostForm(rqst.POST, rqst.FILES, instance=post)
        if form.is_valid():
            # form theke slug and author er option baad daoa hoise,, models.py a slug er blank=True er jnno na likhleo first post add krle error dibena but 2nd post add krte gele error suru hbe and 
            # author akebarei na dile error dibe tai author take  autometically manage krte hbe,jei user logged in thakbe sei jate by default oi post er author hoye jay
            post = form.save() # add a agei author generate kra hoy gese so ekhne temporay save kre alada vabe author implement krte hbe na
    
            # autometic slug generate krar jnno (title theke):
            title = form.cleaned_data['title']
            post.slug = slugify(title) +'-'+str(post.id)
            post.save()
            return redirect('posts')
        else: return redirect('404')
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
