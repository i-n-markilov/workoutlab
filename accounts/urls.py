from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accounts.views import RegisterUserView, ProfileDetailsView

app_name = 'accounts'

profile_patterns = [
    path('details/', ProfileDetailsView.as_view(), name='profile'),
]

auth_patterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

urlpatterns = [
    path('', include(auth_patterns)),
    path('profile/<int:pk>/', include(profile_patterns))
]
