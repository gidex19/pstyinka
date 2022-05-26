from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Audio, Post
# Create your views here.

def home(request):

    return render(request, 'my_app/home.html')

def archive(request):
    audios = Audio.objects.all()
    context = {'audios': audios}
    return render(request, 'my_app/archive.html', context)

def events(request):

    return render(request, 'my_app/events.html')

def gallery(request):

    return render(request, 'my_app/gallery.html')        

def healings(request):

    return render(request, 'my_app/healings.html')

def legacy(request):

    return render(request, 'my_app/legacy.html')

def power_crusades(request):

    return render(request, 'my_app/power_crusades.html')

def blogpage(request):
    posts = Post.objects.all()

    return render(request, 'my_app/blog.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk= pk)
    context = { 'post': post}
    return render(request, 'my_app/post_detail.html', context)
