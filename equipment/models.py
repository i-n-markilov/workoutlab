from django.db import models

from common.models import TimeStampedModel, NameSlugModel


class Equipment(TimeStampedModel, NameSlugModel):
    class TypeChoices(models.TextChoices):
        CARDIO = 'Cardio', 'Cardio'
        FREE_WEIGHTS = 'Free weights', 'Free weights'
        RESISTANCE_MACHINE = 'Resistance machine', 'Resistance machine'
        FUNCTIONAL_TOOL = 'Functional tool', 'Functional tool'


    description = models.TextField(null=True,
                                   blank=True,)

    image_url = models.URLField(null=True,
                                blank=True,)

    type = models.CharField(max_length=100,
                            choices=TypeChoices.choices,)
