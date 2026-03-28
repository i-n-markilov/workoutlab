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
    date_of_birth = forms.DateField(
        input_formats=['%d/%m/%Y', '%d.%m.%Y', '%d-%m-%Y',],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'class': 'datepicker', 'type': 'text'}),
        label="Date of birth:",required=False)

    class Meta:
        model = Profile
        exclude = ('user',)

        labels = {
            'first_name': "First name:",
            'last_name': "Last name:",
            'date_of_birth': "Date of Birth:",
            'profile_picture': "Profile picture:",
        }
    def save(self, commit= True):
        profile = super().save(commit=False)
        if 'first_name' in self.cleaned_data:
            profile.user.first_name = self.cleaned_data['first_name']
        if 'last_name' in self.cleaned_data:
            profile.user.last_name = self.cleaned_data['last_name']

        if commit:
            profile.user.save()
            profile.save()
        return profile