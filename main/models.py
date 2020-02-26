import uuid
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from phone_field import PhoneField


class AdvancedUserManager(BaseUserManager):

    def create_user(self, phone, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not phone:
            raise ValueError('The phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone, password, **extra_fields)


class AdvancedUser(AbstractBaseUser, PermissionsMixin):
    """User additional information"""
    phone_regex     = RegexValidator(regex =   r'^7?\d{10}$', message='Phone number must be in format +7 9999999')
    phone           = models.CharField(validators=[phone_regex], max_length=11, unique=True)
    first_name      = models.CharField(max_length=50)
    surname         = models.CharField(max_length=50)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone'

    objects = AdvancedUserManager()

    def __str__(self):
        return self.phone


class Photo(models.Model):
    id           = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name         = models.CharField(max_length=100, default='Untitled')
    url          = models.URLField(blank=True, null=True)
    photo        = models.ImageField(upload_to='images/%Y/%m/%d')
    owner_id     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_photo')
    users        = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
