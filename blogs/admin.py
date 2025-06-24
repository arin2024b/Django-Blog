from django.contrib import admin
from .models import Category,Blog,About,SocialLink,Comment,Video,Image,React

# nichar class ta autometically slug generate krar jnno create kra hoise
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','category','author','status','is_featured')
    search_fields = ('id','title','category__category_name','status') # models.py a jei sob filed a ForeignKey use kra hoisilo oigulke direct use kra jbe na
    # tai category te __category_name use kra hoise
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin) # ekhne BlogAdmin class ta pass kre daoa hoise
admin.site.register(About)
admin.site.register(Video)
admin.site.register(React)
admin.site.register(Image)
admin.site.register(SocialLink)
admin.site.register(Comment)