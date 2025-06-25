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
    about = models.TextField(max_length=300)
    # github_link = models.URLField(max_length=100,unique=True)
    # linkedin_link = models.URLField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
class SocialLink(models.Model):
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.platform
    
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) # on_delete use kra hoise jate user delete hoy gele comment o delete hoye jay
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE) # blog delete hoile comment o delete hoy jbe
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment
    

class Video(models.Model):
    title = models.CharField(max_length=20)
    video_file = models.FileField(upload_to='videos/')
    views = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - views: {self.views}"


    
class Image(models.Model):
    title = models.CharField(max_length=50)
    image_file = models.ImageField(upload_to='images/')  # Saves to `MEDIA_ROOT/images/`
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class React(models.Model):
    REACTION_CHOICES = [
        ('love', 'Love'),
        ('dislike', 'Dislike'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='reacts')
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)

    def __str__(self):
        return f"{self.user.username} -- {self.video} -- {self.reaction}"
    class Meta:
        unique_together = ('user', 'video')


class VideoComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.video.title} : {self.comment[:30]}..."
    
