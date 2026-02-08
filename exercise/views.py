from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def add_exercise(request: HttpRequest) -> HttpResponse:
    return render(request, 'exercise/add-exercise.html')

def delete_exercise(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'exercise/delete-exercise.html')

def edit_exercise(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'exercise/edit-exercise.html')

def exercise_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'exercise/exercise-list.html')

def exercise_details(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'exercise/exercise-details.html')