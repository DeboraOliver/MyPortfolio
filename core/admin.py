from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin): #personalizar o admin
    list_display = ['name', 'slug', 'technology','created_at']
    search_fields = ['name', 'slug','technology'] #campos que estarão disponiveis p busca


# Register your models here.
admin.site.register(Post, PostAdmin)