from django.contrib import admin
from .models import Page, Post, Song

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_cat', 'page_publish_date', 'user']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_cat', 'post_publish_date', 'user']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'sung_by']
