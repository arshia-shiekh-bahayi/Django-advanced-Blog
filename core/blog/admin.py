from django.contrib import admin
from .models import Post , Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','published_date','created_date', 'updated_date')

"""Registering model Post with PostAdmin design and also model Category to show in admin panel"""
admin.site.register(Post,PostAdmin)
admin.site.register(Category)

