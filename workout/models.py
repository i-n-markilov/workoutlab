from django.db import models
from django.utils.text import slugify

from common.models import TimeStampedModel
from exercise.models import Exercise


class WorkoutPlan(TimeStampedModel):
    name = models.CharField(max_length=100)

    notes = models.TextField(blank=True,
                             null=True)

    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs) -> None:
        if self.pk:
            old_instance = WorkoutPlan.objects.get(pk=self.pk)
            if old_instance.name != self.name:
                self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

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

    order = models.PositiveIntegerField()

    sets = models.PositiveIntegerField()

    reps = models.PositiveIntegerField(blank=True, null=True)

    duration_seconds = models.PositiveIntegerField(blank=True, null=True)

    rest_seconds = models.PositiveIntegerField(default=60)

    class Meta:
        ordering = ["order"]
        unique_together = ("workout", "exercise")