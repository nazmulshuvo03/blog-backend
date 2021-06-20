import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField

from blogBackend.utils import generate_user_id, generate_user_name


class CustomUserManager(BaseUserManager):
    def create_user(self,
                    email,
                    password,
                    first_name=None,
                    last_name=None,
                    username=None
                    ):
        if not email:
            raise ValueError('Enter a valid email')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=generate_user_name(first_name, last_name)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email,
                                password=password,
                                )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(verbose_name="email",
                              max_length=255, unique=True)
    first_name = models.CharField(max_length=700, null=True, blank=True)
    last_name = models.CharField(max_length=700, null=True, blank=True)
    username = models.CharField(
        max_length=255, default='', null=True)
    password = models.CharField(max_length=255)
    profile_image = models.ImageField(
        default='', upload_to='images/', null=True, blank=True)
    linkedin_profile = models.CharField(max_length=700, null=True, blank=True)
    twitter_profile = models.CharField(max_length=700, null=True, blank=True)
    facebook_profile = models.CharField(max_length=700, null=True, blank=True)
    other_links = models.CharField(max_length=700, null=True, blank=True)
    education = models.CharField(max_length=700, null=True, blank=True)
    address = models.CharField(max_length=700, null=True, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser")
    about = models.TextField(blank=True, null=True)
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def get_username(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin
