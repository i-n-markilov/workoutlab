from django.urls import path
from common.api.api_views import StatsAPIView, ListCreateEquipmentApiView

urlpatterns = [
    path('stats/', StatsAPIView.as_view(), name='api-stats'),
    path('equipment/', ListCreateEquipmentApiView.as_view(), name='api-equipment'),
]