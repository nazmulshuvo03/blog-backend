from django.contrib import admin

from .models import Blog, BlogType, BlogTags, Comments, Faq

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('heading', 'author', 'updated_date', 'blog_type', 'power', 'likes', 'dislikes', 'status')
    list_filter = ('status', 'updated_date', 'created_date', 'blog_type')
    search_fields = ('heading', 'slug', 'content', 'blog_type', 'blog_tags')
    actions = ['publish_all', 'decline_all']

    def publish_all(self, request, queryset):
        queryset.update(status="PUBLISHED")

    def decline_all(self, request, queryset):
        queryset.update(status="DECLINED")

admin.site.register(BlogType)
admin.site.register(BlogTags)
admin.site.register(Faq)
