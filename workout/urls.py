from django.urls import path, include
from workout import views

app_name = 'workout'

workout_patterns =[
    path('', views.WorkoutPlanDetailView.as_view(), name='details'),
    path('edit/', views.edit_workout, name='edit'),
    path('delete/', views.WorkoutPlanDeleteView.as_view(), name='delete'),
]

urlpatterns = [
    path('', views.WorkoutPlanListView.as_view(), name='list'),
    path('add-workout/', views.add_workout, name='add'),
    path('<int:pk>/<slug:slug>/', include(workout_patterns)),
]