from django.db import models

from common.models import TimeStampedModel, NameSlugModel
from equipment.models import Equipment


class Exercise(TimeStampedModel, NameSlugModel):
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
