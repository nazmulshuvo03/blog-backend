from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render

from authentication.models import User
from blogs.models import Blog
from authentication.serializers import *
from blogs.serializers import *
from blogBackend.utils import JSONResponse


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data="Only for logged in Users", status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    serialized_user = UserDetailsSerializer(user).data

    try:
        pending_blogs = user.blogs.filter(status='PENDING')
        published_blogs = user.blogs.filter(status='PUBLISHED')
        declined_blogs = user.blogs.filter(status='DECLINED')

        serialized_pending_blogs = BlogListSerializer(pending_blogs, many=True).data
        serialized_published_blogs = BlogListSerializer(published_blogs, many=True).data
        serialized_declined_blogs = BlogListSerializer(declined_blogs, many=True).data

        serialized_user["pending_blogs"] = serialized_pending_blogs
        serialized_user["published_blogs"] = serialized_published_blogs
        serialized_user["declined_blogs"] = serialized_declined_blogs
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return JSONResponse({'code': 200, 'response': serialized_user})


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_ops(request, id):
    try:
        user = get_object_or_404(User, id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
