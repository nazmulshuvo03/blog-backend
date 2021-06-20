from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.blog_list, name='blog_list'),
    path('detail/<slug:blog_slug>', views.blog_detail, name='blog_detail'),
    path('create', views.create_blog, name='create_blog'),
    path('ops/<str:id>', views.blog_ops, name="blog_ops"),
    path('types', views.blog_type_list, name='blog_type_list'),
    path('type/<slug:type_slug>', views.blog_list_on_type, name='blog_list_on_type'),
    path('comment/create', views.create_comment, name='create_comment')
]
