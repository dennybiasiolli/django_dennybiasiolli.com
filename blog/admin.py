from django.contrib import admin

from .models import Category, Tag, Post, Work, Tech

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Tech)
admin.site.register(Work)
