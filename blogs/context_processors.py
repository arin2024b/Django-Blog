# etake custom create krte hbe multiple html file er jnno
# erpor settings.py a jay TEMPLATES er vitore context_processors er vitor app_name.context_processors.function_name dite hbe

from .models import Category,SocialLink
# from assignments.models import SocialLink

def get_categories(rqst):
    categories = Category.objects.all()
    return dict(categories = categories) # ekhn autometically categories gula prottekta html page a dhuke jabe

def get_social_links(rqst):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)