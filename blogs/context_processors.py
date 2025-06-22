# etake custom create krte hbe multiple html file er jnno
# erpor settings.py a jay TEMPLATES er vitore context_processors er vitor app_name.context_processors.function_name dite hbe

from django.shortcuts import render
from .models import Category,SocialLink,Image
# from assignments.models import SocialLink

def get_categories(rqst):
    categories = Category.objects.all()
    return dict(categories = categories) # ekhn autometically categories gula prottekta html page a dhuke jabe

def get_social_links(rqst):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)

def image1(rqst):
    logo = Image.objects.get(title="Logo")
    return {'image1':logo}

def image2(rqst):
    WebsiteName = Image.objects.get(title="WebsiteName")
    return {'image2':WebsiteName}

def image3(rqst):
    BackgroundImage = Image.objects.get(title="BackgroundImage")
    return {'image3':BackgroundImage}