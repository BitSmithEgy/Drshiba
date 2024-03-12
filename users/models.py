from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=255, unique=False, null=True)
    phone_number = PhoneNumberField(_('phone number'), max_length=20, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='Users', blank=True, null=True)
    is_learner = models.BooleanField(default=True)

    #Courses finishe
    d1 = models.BooleanField(default=False)
    d11 = models.BooleanField(default=False)
    d12 = models.BooleanField(default=False)
    d13 = models.BooleanField(default=False)
    d111 = models.BooleanField(default=False)
    d112 = models.BooleanField(default=False)
    d113 = models.BooleanField(default=False)
    d121 = models.BooleanField(default=False)
    d122 = models.BooleanField(default=False)
    d123 = models.BooleanField(default=False)
    d131 = models.BooleanField(default=False)
    d132 = models.BooleanField(default=False)
    d133 = models.BooleanField(default=False)
    d1111 = models.BooleanField(default=False)
    d1112 = models.BooleanField(default=False)
    d1113 = models.BooleanField(default=False)
    d1221 = models.BooleanField(default=False)
    d1222 = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email