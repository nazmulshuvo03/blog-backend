from django.contrib import admin

from .models import Blog, BlogType, BlogTags, Comments

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Blog)
admin.site.register(BlogType)
admin.site.register(BlogTags)
