from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.blog_list, name='blog_list'),
    path('detail/<slug:blog_slug>', views.blog_detail, name='blog_detail'),
    path('create', views.create_blog, name='create_blog'),
    path('ops/<str:id>', views.blog_ops, name="blog_ops")
]
