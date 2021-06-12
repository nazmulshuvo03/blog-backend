from django.contrib import admin

from .models import Blog, BlogType, BlogTags

admin.site.register(Blog)
admin.site.register(BlogType)
admin.site.register(BlogTags)
