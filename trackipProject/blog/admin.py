from django.contrib import admin
from .models import Post, Contact

# PostAdmin
@admin.register(Post)
class PostAdminPanel(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

# ContactAdmin
@admin.register(Contact)
class contactAdminPanel(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message']
