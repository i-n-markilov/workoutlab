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

#imports for those models are here because Django imports them before finding the AppUser
from equipment.models import Equipment
from exercise.models import Exercise
from workout.models import WorkoutPlan

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

    favourite_equipments = models.ManyToManyField(Equipment,
                                                 blank=True,
                                                 related_name='user_favourite')

    favourite_exercises = models.ManyToManyField(Exercise,
                                                 blank=True,
                                                 related_name='user_favourite')

    favourite_workoutplans = models.ManyToManyField(WorkoutPlan,
                                                   blank=True,
                                                   related_name='user_favourite')