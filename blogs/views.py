from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Blog,Category,Comment
from django.db.models import Q # eta import kora hoiche or operator usage er jnno

# Create your views here.
def posts_by_category(rqst,category_id):
    posts = Blog.objects.filter(status = 'Published',category = category_id)
    # return HttpResponse(posts)
    category = get_object_or_404(Category,pk=category_id) # category_id dara category er nam ta ta bair krar jnno
    # tobe templates a jei 404.html page ta create kra hoise etake direct nia nibe kno views a connect kra charai .. r jdi 404.html create kra na hoito tahile default error msg dekhaito
    # 404.html page take error hisebe dekhanor jnno settings.py te jay DEBUG = Flase krte hbe and ALLOWED_HOST = ['*'] dite hbe jate jkno host ke nia nay
    # uporer ta baad dia nichar try-except use kre 404 error na dia home page back krano hoise
    # try:
    #     category = Category.objects.get(pk = category_id)
    # except:
    #     return redirect('home')
    
    context = {
        'posts':posts,
        'category':category,
    }
    return render(rqst,'posts_by_category.html',context)

def blogs(rqst,slug):
    single_blog = get_object_or_404(Blog, slug=slug, status = 'Published')
    
    # get Comments
    if rqst.method == 'POST':
        comment = Comment()
        comment.user = rqst.user
        comment.blog = single_blog
        comment.comment = rqst.POST['comment'] # commnet.comment er 2nd comment ta models.py er Comment class er comment..[] er vitorer comment ta blogs.html er textfiler er name attribute ta
        comment.save()
        return HttpResponseRedirect(rqst.path_info) # oi same page reload krar jnno eta use hoy
    
    comments = Comment.objects.filter(blog = single_blog)
    comment_count = comments.count() 
    
    context = {
        'single_blog':single_blog,
        'cmnts':comments,
        'cmnt_count':comment_count,
    }
    return render(rqst,'blogs.html',context)

def search(rqst):
    keyword = rqst.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_desc__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published') # icontains er i means case sensitive.. ekhne upper case,lower case matter kore na
    context = {
        'blogs':blogs,
        'kywrd':keyword,
    }
    return render(rqst,'search.html',context)
