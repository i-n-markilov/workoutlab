from django.db import models
from django.db.models import Q

class VisibilityQuerySet(models.QuerySet):
    def visible_for_user(self, user):
        if user.is_authenticated:
            return self.filter(Q(private=False) | Q(user=user))
        return self.filter(private=False)

    def owned_by(self, user):
        return self.filter(user=user)

    def search(self, query):
        if query:
            return self.filter(name__icontains=query)
        return self