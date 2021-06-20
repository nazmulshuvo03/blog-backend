import uuid
from django.db import models
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from datetime import datetime, timedelta
from django.utils.text import slugify

from authentication.models import User


class BlogType(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True)
    slug = models.SlugField(max_length=2000, editable=False,
                            default='', unique=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BlogType, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class BlogTags(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    header_image = models.ImageField(
        default='', upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='id', related_name='Author', null=True, blank=True)
    heading = models.CharField(max_length=2000)
    content = RichTextUploadingField()
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)
    description = models.CharField(max_length=2000, default="")
    is_active = models.BooleanField(default=True)
    blog_type = models.ForeignKey(
        BlogType, default=None, on_delete=models.SET_DEFAULT, to_field='name', related_name='Type', null=True, blank=True)
    blog_tags = models.ManyToManyField(
        BlogTags, related_name="Tags", blank=True)
    slug = models.SlugField(max_length=2000, editable=False,
                            default='', unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ['-created_date']
