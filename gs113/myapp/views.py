from django.shortcuts import render
from .models import Page, Post, Song, User

def home(request):
    return render(request, 'myapp/home.html')

def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email='mkshah141@gmail.com')
    data3 = User.objects.filter(mypage__page_cat='Programming')
    data4 = User.objects.filter(post__post_publish_date='2021-02-26')
    data5 = User.objects.filter(song__song_duration=3)
    return render(request, 'myapp/user.html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

def show_page_data(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(page_cat='Programming')
    data3 = Page.objects.filter(user__email='mkshah141@gmail.com')
    return render(request, 'myapp/page.html', {'data1': data1, 'data2': data2, 'data3': data3})

def show_post_data(request):
    data1 = Post.objects.all()
    data2 = Post.objects.filter(post_publish_date='2020-05-28')
    data3 = Post.objects.filter(user__username='sonam')
    return render(request, 'myapp/post.html', {'data1': data1, 'data2': data2, 'data3': data3})

def show_song_data(request):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(song_duration=3)
    data3 = Song.objects.filter(user__username='sonam')
    return render(request, 'myapp/song.html', {'data1': data1, 'data2': data2, 'data3': data3})
