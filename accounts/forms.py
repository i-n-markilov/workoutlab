from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm

from accounts.models import AppUser, Profile


class AppUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = AppUser
        fields = ('email',)

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AppUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

        labels = {
            'first_name': "First Name:",
            'last_name': "Last Name:",
            'date_of_birth': "Date of Birth:",
            'profile_picture': "Profile Picture:",
        }