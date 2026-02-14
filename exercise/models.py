from django.db import models
from django.utils.text import slugify

from common.models import TimeStampedModel
from equipment.models import Equipment


class Exercise(TimeStampedModel):
    class MuscleGroup(models.TextChoices):
        CHEST = 'Chest', 'Chest'
        BACK = 'Back', 'Back'
        LEGS = 'Legs', 'Legs'
        SHOULDERS = 'Shoulders', 'Shoulders'
        ARMS = 'Arms', 'Arms'
        CORE = 'Core', 'Core'

    class DifficultyChoices(models.TextChoices):
        EASY = 'Easy', 'Easy'
        MEDIUM = 'Medium', 'Medium'
        HARD = 'Hard', 'Hard'

    name = models.CharField(max_length=100,
                            unique=True)

    difficulty = models.CharField(max_length=10,
                                  choices=DifficultyChoices.choices,)

    description = models.TextField(blank=True, null=True)

    instructions = models.TextField(blank=True, null=True)

    primary_muscle_group = models.CharField(max_length=50,
                                            choices=MuscleGroup.choices,)

    secondary_muscle_group = models.CharField(max_length=50,
                                              choices=MuscleGroup.choices,
                                              null=True,
                                              blank=True)

    equipment = models.ManyToManyField(
        Equipment,
        related_name='exercises',
        blank=True,
    )

    is_bodyweight = models.BooleanField(default=False)

    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs) -> None:
        if self.pk:
            old_instance = Exercise.objects.get(pk=self.pk)
            if old_instance.name != self.name:
                self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

