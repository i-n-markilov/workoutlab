from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import AppUser, Profile


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email')

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