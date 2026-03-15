from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from accounts.forms import AppUserCreationForm
from accounts.models import Profile

UserModel = get_user_model()

class RegisterUserView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/user/register.html'
    success_url = reverse_lazy('accounts:login')

class ProfileDetailsView(TemplateView):
    model = Profile
    template_name = 'accounts/profile/profile-details.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    ...