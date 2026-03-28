from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models



class AppUser(AbstractUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    username = models.CharField(max_length = 50,
                                unique=True,)

    email = models.EmailField(max_length=100,
                              unique=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username

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