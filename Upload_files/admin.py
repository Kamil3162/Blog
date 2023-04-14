from django.contrib import admin
from Upload_files import models
# Register your models here.

"""
    Using this part we can manage what we display in the admin panel:
    so using decorator we create a class and input a option whose we want to filter
"""


@admin.register(models.Image)
class AdminManage(admin.ModelAdmin):
    list_display = ['post', 'image']


@admin.register(models.Post)
class AdminManage(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.PostComments)
class AdminManage(admin.ModelAdmin):
    list_display = ['user', 'post']
    search_fields = ['user']
