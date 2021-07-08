import uuid
from django.db import models
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
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
    status_choices = (
        ('PUBLISHED', 'PUBLISHED'),
        ('PENDING', 'PENDING'),
        ('DECLINED', 'DECLINED')
    )
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    header_image = models.ImageField(
        default='', upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='id', related_name='Author', null=True, blank=True)
    heading = models.CharField(max_length=1000)
    meta_title = models.CharField(max_length=1000, default="", null=True, blank=True)
    page_title = models.CharField(max_length=1000)
    content = RichTextUploadingField()
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)
    description = models.CharField(max_length=2000, default="", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    blog_type = models.ForeignKey(
        BlogType, default=None, on_delete=models.SET_DEFAULT, to_field='name', related_name='Type', null=True, blank=True)
    blog_tags = models.ManyToManyField(
        BlogTags, related_name="Tags", blank=True)
    slug = models.SlugField(max_length=2000, editable=False,
                            default='', unique=True)
    likes = models.IntegerField(default=0, blank=True)
    dislikes = models.IntegerField(default=0, blank=True)
    power = models.FloatField(default=0, blank=True)
    status = models.CharField(max_length=15, choices=status_choices, default='PENDING')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ['-created_date']


class Faq(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255, null=True, unique=True)
    answer = models.CharField(max_length=255, null=True, unique=True)

    def __str__(self) -> str:
        return self.question + " -> " + self.answer

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name="email",
                              max_length=255, null=True, blank=True)
    body = models.TextField(max_length=3000)
    created_on = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    class Meta:
        ordering = ['created_on']