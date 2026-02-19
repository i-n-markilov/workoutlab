from django.urls import path, include
from equipment import views

app_name = 'equipment'

equipment_patterns =[
    path('', views.EquipmentDetailView.as_view(), name='details'),
    path('edit/', views.EquipmentEditView.as_view(), name='edit'),
    path('delete/', views.EquipmentDeleteView.as_view(), name='delete'),
]

urlpatterns = [
    path('', views.EquipmentListView.as_view(), name='list'),
    path('add-equipment/', views.EquipmentCreateView.as_view(), name='add'),
    path('<int:pk>/<slug:slug>/', include(equipment_patterns)),
]
