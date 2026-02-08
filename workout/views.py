from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def add_workout(request: HttpRequest) -> HttpResponse:
    return render(request, 'workout/add-workout.html')

def delete_workout(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'workout/delete-workout.html')

def edit_workout(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'workout/edit-workout.html')

def workout_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'workout/workout-list.html')

def workout_details(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'workout/workout-details.html')