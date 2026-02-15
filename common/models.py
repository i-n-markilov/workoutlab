from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.text import slugify

from common.validators import validate_alphanumeric_spaces


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class NameSlugModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100,
                            unique=True,
                            validators=[validate_alphanumeric_spaces], )

    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs) -> None:
        if self.pk:
            old_instance = self.__class__.objects.get(pk=self.pk)
            if old_instance.name != self.name:
                self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class MotivationMessage(models.Model):
    text = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.text