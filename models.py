from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.db import models
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Ensure the necessary fields for a superuser are set to True
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Optional
    address = models.TextField(blank=True, null=True)  # Optional
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # For admin privileges
    is_admin = models.BooleanField(default=False)  # To distinguish admin from regular users
    signup_date = models.DateTimeField(default=timezone.now)  # Automatically sets the signup date

    objects = CustomUserManager()  # Use the custom user manager

    USERNAME_FIELD = 'email'  # Unique identifier for authentication
    REQUIRED_FIELDS = ['name']  # Fields required for superuser creation

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6, null=True)
    verification_code_created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for verification code

    def __str__(self):
        return f'Profile of {self.user.email}'

class Admin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    signup_date = models.DateTimeField(default=timezone.now)  # Automatically sets the signup date

    def __str__(self):
        return self.username
