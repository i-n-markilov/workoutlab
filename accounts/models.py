from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    email = models.EmailField(max_length=100,
                              unique=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    objects = AppUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(AppUser,
                                on_delete=models.CASCADE,
                                primary_key=True)

    first_name = models.CharField(max_length=100,
                                  null=True,
                                  blank=True)

    last_name = models.CharField(max_length=100,
                                 null=True,
                                 blank=True)

    date_of_birth = models.DateField(blank=True,
                                     null=True)

    profile_pic = models.URLField(blank=True,
                                  null=True)