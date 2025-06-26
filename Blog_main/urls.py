"""
URL configuration for Blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
# nichar 2 ta import kra hoise media file ke urlpatterns er sthe concatinate krar jnno
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as AppViews # as dia kisu dile views er jaygay oita likha jabe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('category/',include('blogs.urls')),
    path('blogs/<slug:slug>/',AppViews.blogs,name='blogs'),
    
    # Search endpoint
    path('search/',AppViews.search,name='search'),
    
    # for register-logIn functionality
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    
    # for logOut functionality
    path('logout/',views.logout,name='logout'),
    
    # Dashboards
    path('dashboard/',include('dashboards.urls')),
    
    # Video
    path('uploadV/', views.upload_video, name='upload_video'),
    
    # Image
    path('uploadI/', views.upload_image, name='upload_image'),
    
    # For Reacts
    path('react/<int:video_id>/', views.toggle_reaction, name='toggle_reaction'),
    
    # For Comments
    path('comment/<int:video_id>/', views.add_comment, name='add_comment'),
    path('comments/<int:video_id>/', views.get_comments, name='get_comments'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    
    # For Views
    path('view/<int:video_id>/', views.increment_view, name='increment_view'),
    
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
