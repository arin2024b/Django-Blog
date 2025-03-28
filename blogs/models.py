from django.db import models
# Blog er author a jei User ta daoa hoise etake import krte hbe
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True) # unique = True krle nam ta unique hisbe nibe,jeta second time use kra jbe na
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # admin panel a wrong spelling show krbe plural form er 
    # eta thik krar jnno 
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name
    
    
# nichar Blog model er status filed er jnno:
STATUS_CHOICES = (
    ("Draft","Draft"),
    ("Published","Published")
)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%y/%m/%d') # etar mane uploads nam er folder a year,month,date er sthe image gula save hbe dynamically
    short_desc = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    about = models.TextField(max_length=200)
    github_link = models.CharField(max_length=100,unique=True)
    linkedin_link = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)