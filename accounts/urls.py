from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include, reverse_lazy

from accounts.views import RegisterUserView

app_name = 'accounts'

profile_patterns = [

]

auth_patterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

urlpatterns = [
    path('', include(auth_patterns)),
    path('profile/<int:pk>/', include(profile_patterns))
]
