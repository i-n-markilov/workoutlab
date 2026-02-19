from django.urls import path, include
from exercise import views

app_name = 'exercise'

exercise_patterns =[
    path('', views.ExerciseDetailView.as_view(), name='details'),
    path('edit/', views.ExerciseEditView.as_view(), name='edit'),
    path('delete/', views.ExerciseDeleteView.as_view(), name='delete'),
]

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='list'),
    path('add-exercise/', views.ExerciseCreateView.as_view(), name='add'),
    path('<int:pk>/<slug:slug>/', include(exercise_patterns)),
]
