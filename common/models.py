from django.db import models


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class MotivationMessage(models.Model):
    text = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
