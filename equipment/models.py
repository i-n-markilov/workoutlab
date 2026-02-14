from django.db import models
from django.utils.text import slugify

from common.models import TimeStampedModel


class Equipment(TimeStampedModel):
    class TypeChoices(models.TextChoices):
        CARDIO = 'Cardio', 'Cardio'
        FREE_WEIGHTS = 'Free weights', 'Free weights'
        RESISTANCE_MACHINE = 'Resistance machine', 'Resistance machine'
        FUNCTIONAL_TOOL = 'Functional tool', 'Functional tool'

    name = models.CharField(max_length=100,
                            unique=True)
    description = models.TextField(null=True,
                                   blank=True)
    type = models.CharField(max_length=100,
                            choices=TypeChoices.choices,)

    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs) -> None:
        if self.pk:
            old_instance = Equipment.objects.get(pk=self.pk)
            if old_instance.name != self.name:
                self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name