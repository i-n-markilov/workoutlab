from django.db import models

from common.models import TimeStampedModel, NameSlugModel
from exercise.models import Exercise
from workout.validators import min_value_validator


class WorkoutPlan(TimeStampedModel, NameSlugModel):

    notes = models.TextField(blank=True,
                             null=True)

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name="items"
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE
    )

    order = models.PositiveIntegerField(validators=[min_value_validator])

    sets = models.PositiveIntegerField(validators=[min_value_validator])

    reps = models.PositiveIntegerField(blank=True, null=True,validators=[min_value_validator])

    duration_seconds = models.PositiveIntegerField(blank=True, null=True, validators=[min_value_validator])

    rest_seconds = models.PositiveIntegerField(default=60, validators=[min_value_validator])

    class Meta:
        ordering = ["order"]
        unique_together = ("workout", "exercise")
