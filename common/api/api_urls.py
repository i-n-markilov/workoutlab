from django.urls import path
from common.api.api_views import StatsAPIView

urlpatterns = [
    path('stats/', StatsAPIView.as_view(), name='api-stats'),
]