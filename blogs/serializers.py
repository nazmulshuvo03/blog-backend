from django.db.models import fields
from rest_framework import serializers
from .models import *
from authentication.serializers import UserDetailsSerializer


class BlogListSerializer(serializers.ModelSerializer):
    author = UserDetailsSerializer()

    class Meta:
        model = Blog
        fields = [
            'id',
            'heading',
            'header_image',
            'created_date',
            'slug',
            'author',
            'blog_type',
            'blog_tags'
        ]


class BlogDetailSerializer(serializers.ModelSerializer):
    author = UserDetailsSerializer()

    class Meta:
        model = Blog
        fields = '__all__'


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogType
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'