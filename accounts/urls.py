from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include, reverse_lazy

from accounts.views import RegisterUserView, ProfileDetailsView, ProfileUpdateView, ProfileDeleteView

app_name = 'accounts'

profile_patterns = [
    path('details/', ProfileDetailsView.as_view(), name='profile'),
    path('edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]

auth_patterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

urlpatterns = [
    path('', include(auth_patterns)),
    path('profile/<int:pk>/', include(profile_patterns)),
    path('password-change/',PasswordChangeView.as_view(
        template_name='accounts/user/password-change.html',
        success_url=reverse_lazy('accounts:password_change_done')), name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(template_name='accounts/user/password-change-done.html'), name='password_change_done'),

]
