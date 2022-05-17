from gzip import READ
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission)
from django.urls import reverse



class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser duhet te jete is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser duhet te jete is_superuser=True.')

        return self.create_user(email, first_name, password, **other_fields)

    def create_user(self, email, first_name, password, **other_fields):

        if not email:
            raise ValueError('Duhet te vendosesh nje email')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True)
    last_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    image = models.ImageField(
        verbose_name= "image",
        help_text="Upload a property image",
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name="Alturnative text",
        help_text="Please add alturnative text",
        max_length=255,
        null=True,
        blank=True,
    )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        db_table = "agent_user"
        verbose_name = "Agent"
        verbose_name_plural = "Agents"
    
    def get_absolute_url(self):
        return reverse('agent:agent_properties', args=[self.slug])

    def __str__(self):
        return self.first_name