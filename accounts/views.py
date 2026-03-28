from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from accounts.forms import AppUserCreationForm, ProfileForm
from accounts.models import Profile

UserModel = get_user_model()

class RegisterUserView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/user/register.html'
    success_url = reverse_lazy('accounts:login')

class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile/profile-details.html'

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile/profile-edit.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})

class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile/profile-delete.html'
    success_url = reverse_lazy('common:home')

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def form_valid(self, form):
        success_url = self.get_success_url()
        user = self.request.user
        logout(self.request)
        user.delete()
        return redirect(success_url)