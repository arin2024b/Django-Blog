from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from blogs.models import Category,Blog,About,Video,Image,React,VideoComment
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm # login html er authentication er jnno 
from django.contrib import auth # user data gulake entered dara er sathe match kranor jnno import kora hoise
from Blog_main.forms import VideoForm,ImageForm
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def home(request):
    # return HttpResponse('Hello Mc')
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True,status = 'Published').order_by("?")
    posts = Blog.objects.filter(is_featured = False, status = 'Published').order_by('?')
    about = About.objects.all()
    # videos = Video.objects.all().order_by('?')
    # Add reaction counts to videos
    videos = Video.objects.annotate(
        love_count=Count('reacts', filter=Q(reacts__reaction='love')),
        dislike_count=Count('reacts', filter=Q(reacts__reaction='dislike'))
    ).order_by('?')

    context = {
        # 'categories': categories, # jehetu context_processors.py te already daoa hoise tai ar alada vabe daoar drkr nau
        'featured_posts': featured_posts,
        'posts':posts,
        'about':about,
        'videos':videos,
    }
    return render(request,'home.html',context)

@login_required
def toggle_reaction(request, video_id):
    if request.method == 'POST':
        video = Video.objects.get(id=video_id)
        reaction_type = request.POST.get('reaction')
        
        # Check if user already reacted
        existing_reaction = React.objects.filter(user=request.user, video=video).first()
        
        if existing_reaction:
            if existing_reaction.reaction == reaction_type:
                # Remove reaction if same type
                existing_reaction.delete()
            else:
                # Change reaction type
                existing_reaction.reaction = reaction_type
                existing_reaction.save()
        else:
            # Create new reaction
            React.objects.create(user=request.user, video=video, reaction=reaction_type)
        
        # Get updated counts
        love_count = React.objects.filter(video=video, reaction='love').count()
        dislike_count = React.objects.filter(video=video, reaction='dislike').count()
        
        return JsonResponse({
            'love_count': love_count,
            'dislike_count': dislike_count
        })
    
    return JsonResponse({'error': 'Invalid request'})

@login_required
def add_comment(request, video_id):
    if request.method == 'POST':
        video = Video.objects.get(id=video_id)
        comment_text = request.POST.get('comment')
        
        if comment_text.strip():
            comment = VideoComment.objects.create(
                user=request.user,
                video=video,
                comment=comment_text.strip()
            )
            
            return JsonResponse({
                'success': True,
                'comment': {
                    'id': comment.id,
                    'username': comment.user.username,
                    'comment': comment.comment,
                    'created_at': comment.created_at.strftime('%b %d, %Y at %I:%M %p')
                }
            })
        
    return JsonResponse({'error': 'Invalid request'})

def get_comments(request, video_id):
    video = Video.objects.get(id=video_id)
    comments = VideoComment.objects.filter(video=video).order_by('-created_at')
    
    from datetime import datetime
    from zoneinfo import ZoneInfo
    bd_time = datetime.now(ZoneInfo('Asia/Dhaka'))
    
    comments_data = [{
        'id': comment.id,
        'username': comment.user.username,
        'comment': comment.comment,
        'created_at': bd_time.strftime('%b %d, %Y at %H:%M BDT')
        # 'created_at':comment.created_at.strftime('%b %d, %Y at %I:%M %p')
    } for comment in comments]
    
    return JsonResponse({
        'comments': comments_data,
        'count': comments.count()
    })

@login_required
def increment_view(request, video_id):
    if request.method == 'POST':
        try:
            video = Video.objects.get(id=video_id)
            video.views += 1
            video.save()
            return JsonResponse({
                'success': True,
                'views': video.views
            })
        except Video.DoesNotExist:
            return JsonResponse({'error': 'Video not found'})
    
    return JsonResponse({'error': 'Invalid request'})

def register(rqst):
    if rqst.method == 'POST':
        form = RegistrationForm(rqst.POST)
        if form.is_valid(): 
            form.save()
            return redirect('login')
        # else : print(form.errors)
    else:
        form = RegistrationForm()
        
    context = {
        'frm' : form,
    }
    return render(rqst,'register.html',context)

def login(rqst):
    if rqst.method == 'POST':
        form = AuthenticationForm(rqst,rqst.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username,password=password)
            if user is not None: auth.login(rqst, user)
            return redirect('home')
        else: print(form.errors)
    form = AuthenticationForm()
    context={
        'frm':form,
    }
    return render(rqst,'login.html',context)

def logout(rqst):
    auth.logout(rqst)
    return redirect('home')

def upload_video(request):
    videos = Video.objects.all().order_by('-uploaded_at')
    
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_video')
    else:
        form = VideoForm()
    return render(request, 'dashboard/upload_video.html', {'form': form,'videos':videos,})

def upload_image(request):
    images = Image.objects.all().order_by('-uploaded_at')
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ImageForm()
    return render(request, 'dashboard/upload_image.html', {'form': form,'images':images,})