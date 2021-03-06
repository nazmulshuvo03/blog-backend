from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.blog_list, name='blog_list'),
    path('detail/<slug:blog_slug>', views.blog_detail, name='blog_detail'),
    path('create', views.create_blog, name='create_blog'),
    path('ops/<str:id>', views.blog_ops, name="blog_ops"),
    path('types', views.blog_type_list, name='blog_type_list'),
    path('types_with_blog', views.blog_type_list_with_blogs, name='blog_type_list_with_blogs'),
    path('types_with_published_blog', views.blog_type_list_with_published_blogs, name='blog_type_list_with_published_blogs'),
    path('blogs_without_type', views.blogs_without_type, name='blogs_without_type'),
    path('type/<slug:type_slug>', views.blog_list_on_type, name='blog_list_on_type'),
    path('comment/create', views.create_comment, name='create_comment'),
    path('like/<slug:blog_slug>', views.like_a_blog, name='like_a_blog'),
    path('dislike/<slug:blog_slug>', views.dislike_a_blog, name='dislike_a_blog'),
    path('faqs/list', views.get_faqs, name='get_faqs'),
    path('faqs/create', views.create_faqs, name='create_faq'),
]
