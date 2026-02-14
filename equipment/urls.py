from django.urls import path, include
from equipment import views

app_name = 'equipment'

equipment_patterns =[
    path('', views.equipment_details, name='details'),
    path('edit/', views.edit_equipment, name='edit'),
    path('delete/', views.delete_equipment, name='delete'),
]

urlpatterns = [
    path('', views.equipment_list, name='list'),
    path('add-equipment/', views.add_equipment, name='add'),
    path('<int:pk>/<slug:slug>/', include(equipment_patterns)),
]
