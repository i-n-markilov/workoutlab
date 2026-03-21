from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from common.managers import VisibilityQuerySet
from common.models import TimeStampedModel, NameSlugModel

UserModel = get_user_model()

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

    user = models.ForeignKey(UserModel,
                             on_delete=models.CASCADE,
                             related_name='equipment',
                             null=True,
                             blank=True,)

    private = models.BooleanField(default=False)

    system_generated = models.BooleanField(default=False)

    objects = VisibilityQuerySet.as_manager()