from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from blogs.models import Video,Image

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username','password1','password2') # password1 is for typing password and password2 for confirm password and it's default in django
        
        
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image_file']
        