from django.db import models


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class DifficultyModel(models.Model):
    class Meta:
        abstract = True

    class DifficultyChoices(models.TextChoices):
        EASY = 'Easy', 'Easy'
        MEDIUM = 'Medium', 'Medium'
        HARD = 'Hard', 'Hard'

    difficulty = models.CharField(max_length=10,
                                  choices=DifficultyChoices.choices,)