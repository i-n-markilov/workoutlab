from django.urls import path, include
from exercise import views

app_name = 'exercise'

exercise_patterns =[
    path('', views.exercise_details, name='details'),
    path('edit/', views.edit_exercise, name='edit'),
    path('delete/', views.delete_exercise, name='delete'),
]

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='list'),
    path('add-exercise/', views.add_exercise, name='add'),
    path('<int:pk>/<slug:slug>/', include(exercise_patterns)),
]
