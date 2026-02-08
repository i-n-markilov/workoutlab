from django.db import models
from django.utils.text import slugify

from common.models import TimeStampedModel


class Exercise(TimeStampedModel):
    class MuscleGroup(models.TextChoices):
        CHEST = 'Chest', 'Chest'
        BACK = 'Back', 'Back'
        LEGS = 'Legs', 'Legs'
        SHOULDERS = 'Shoulders', 'Shoulders'
        ARMS = 'Arms', 'Arms'
        CORE = 'Core', 'Core'

    name = models.CharField(max_length=100,
                            unique=True)
    description = models.TextField(blank=True, null=True)

    primary_muscle_group = models.CharField(max_length=50,
                                            choices=MuscleGroup.choices,)

    secondary_muscle_group = models.CharField(max_length=50,
                                               choices=MuscleGroup.choices,
                                               null=True,)

    equipment = models.ManyToManyField(
        'Equipment',
        related_name='exercises',
        blank=True,
        null=True,
    )

    is_bodyweight = models.BooleanField(default=False)

    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.name}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

