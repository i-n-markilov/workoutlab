from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from accounts.forms import AppUserCreationForm

UserModel = get_user_model()

class RegisterUserView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('common:home')

class ProfileDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile.html'