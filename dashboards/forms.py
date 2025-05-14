from django import forms
from blogs.models import Category,Blog

from django.contrib.auth.forms import UserCreationForm # eta Block_main er forms.py theke import kra hoise
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
       model = Category
       fields = '__all__'
       
class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','featured_image','short_desc','blog_body','status','is_featured')
        
class UserForm(UserCreationForm): # ekhane forms.ModelForm er jaygay UserCreationForm use kra hoise jeta agei onno forms.py te create kra chilo.ekhne password creation er options thakbe
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','is_active','is_staff','groups','user_permissions')
        
class EditUserForm(forms.ModelForm): # ekhne password changing er option thakbena
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','is_active','is_staff','groups','user_permissions')