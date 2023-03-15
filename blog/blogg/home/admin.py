from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ArticleQuestion)
class ArticleQuestionAdmin(admin.ModelAdmin):
    list_display = ['article']
    search_fields = ['article']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

admin.site.register(Question)
@admin.register(Article) # Отображение в админ панели модели Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'body','date']
    list_filter = ['title','date']
    search_fields = ['title']
    
@admin.register(User) # Отображение в админ панели модели User
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','allow_admin']
    list_filter = ['username','allow_admin']
    search_fields = ['username']

    