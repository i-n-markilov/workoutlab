from django.db import models
from django.db.models import Q

class VisibilityQuerySet(models.QuerySet):
    def visible_for_user(self, user):
        if user.is_authenticated:
            if user.is_staff or user.is_superuser or user.groups.filter(name='Moderator').exists():
                return self.all()
            else:
                return self.filter(Q(private=False) | Q(user=user))
        return self.filter(private=False)

    def editable_by_user(self, user):
        if user.is_authenticated:
            if user.is_staff or user.is_superuser or user.groups.filter(name='Moderator').exists():
                return self.all()
        return self.filter(user=user)


    def search(self, query):
        if query:
            return self.filter(name__icontains=query)
        return self