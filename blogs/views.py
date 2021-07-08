from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework import status
from rest_framework.response import Response

from blogBackend.utils import JSONResponse
from .models import *
from .serializers import *


def index(request):
    return HttpResponse("Hello, You are at Pvot Blog index")


def blog_list(request):
    blogs = Blog.objects.all()
    serialized_data = BlogListSerializer(
        blogs, many=True, context={'request': request}).data
    return JSONResponse({'code': 200, 'response': serialized_data})


def blog_detail(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    comments = blog.comments.all()
    faqs = blog.faqs.all()
    serialized_blog = BlogDetailSerializer(blog).data
    serialized_comments = CommentSerializer(comments, many=True).data
    serialized_faqs = FaqViewSerializer(faqs, many=True).data
    serialized_blog['comments'] = serialized_comments
    serialized_blog['faqs'] = serialized_faqs
    return JSONResponse({'code': 200, 'response': serialized_blog})


def blog_type_list(request):
    types = BlogType.objects.all()
    serialized_types = BlogTypeSerializer(types, many=True).data
    return JSONResponse({'code': 200, 'response': serialized_types})

def blog_type_list_with_blogs(request):
    types = BlogType.objects.all()
    serialized_types = BlogTypeSerializer(types, many=True).data
    for t in serialized_types:
        blogs = Blog.objects.filter(blog_type=t['name'])
        serialized_blogs = BlogListSerializer(blogs, many=True).data
        t['blogs'] = serialized_blogs

    other_blogs = Blog.objects.filter(blog_type=None)
    serialized_other_blogs = BlogListSerializer(
        other_blogs, many=True, context={'request': request}).data

    serialized_types.append({'id': len(serialized_types)+1, 'name': 'No Type', 'slug': 'no_type', 'blogs': serialized_other_blogs})
    return JSONResponse({'code': 200, 'response': serialized_types})

def blogs_without_type(request):
    blogs = Blog.objects.filter(blog_type=None)
    serialized_data = BlogListSerializer(
        blogs, many=True, context={'request': request}).data
    return JSONResponse({'code': 200, 'response': serialized_data})

def blog_list_on_type(request, type_slug):
    try:
        type_of_blog = get_object_or_404(BlogType, slug=type_slug)
        blogs = Blog.objects.filter(blog_type=type_of_blog)
        serialized_blogs = BlogListSerializer(blogs, many=True).data
        return JSONResponse({'code': 200, 'response': serialized_blogs})
        
    except BlogType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_comment(request):
    if request.method == 'POST':
        serialized_comment = CommentSerializer(data=request.data)
        if serialized_comment.is_valid():
            serialized_comment.save()
            return Response(serialized_comment.data, status=status.HTTP_201_CREATED)
        return Response(serialized_comment.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_faqs(request):
    if request.method == 'POST':
        serialized_faq = FaqCreateSerializer(data=request.data, many=True)
        if serialized_faq.is_valid():
            serialized_faq.save()
            return Response(serialized_faq.data, status=status.HTTP_201_CREATED)
        return Response(serialized_faq.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([AllowAny])
def like_a_blog(request, blog_slug):
    if request.method == 'PATCH':
        blog = get_object_or_404(Blog, slug=blog_slug)
        new_likes = blog.likes + 1
        new_power = blog.power + 1
        serializer = CreateBlogSerializer(
            blog, data={'likes': new_likes, 'power': new_power}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([AllowAny])
def dislike_a_blog(request, blog_slug):
    if request.method == 'PATCH':
        blog = get_object_or_404(Blog, slug=blog_slug)
        new_dislikes = blog.dislikes + 1
        new_power = blog.power - 1
        serializer = CreateBlogSerializer(
            blog, data={'dislikes': new_dislikes, 'power': new_power}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    if request.method == 'POST':
        serialized_data = CreateBlogSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def blog_ops(request, id):
    try:
        blog = get_object_or_404(Blog, id=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogDetailSerializer(blog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CreateBlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = CreateBlogSerializer(
            blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
