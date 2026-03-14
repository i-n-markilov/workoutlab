from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm

from accounts.models import AppUser


class AppUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = AppUser
        fields = ('email',)

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AppUser
