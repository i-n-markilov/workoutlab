from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from exercise.forms import ExerciseCreateForm, ExerciseEditForm
from exercise.models import Exercise


# Create your views here.
def add_exercise(request: HttpRequest) -> HttpResponse:
    form = ExerciseCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('exercise:list')

    context = {'form': form}

    return render(request, 'exercise/add-exercise.html', context)

def delete_exercise(request: HttpRequest, pk: int, slug: str) -> HttpResponse:
    exercise = get_object_or_404(Exercise, pk=pk, slug=slug)

    if request.method == 'POST':
        exercise.delete()
        return redirect('exercise:list')

    context = {'exercise': exercise}

    return render(request, 'exercise/delete-exercise.html', context)

def edit_exercise(request: HttpRequest, pk: int, slug: str) -> HttpResponse:
    exercise = get_object_or_404(Exercise, pk=pk, slug=slug)
    form = ExerciseEditForm(request.POST or None, instance=exercise)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('exercise:list')

    context = {'form': form, 'exercise': exercise}

    return render(request, 'exercise/edit-exercise.html', context)

def exercise_list(request: HttpRequest) -> HttpResponse:
    exercises = Exercise.objects.all().order_by('name', 'created')

    context = {'exercises': exercises}
    return render(request, 'exercise/exercise-list.html', context)

def exercise_details(request: HttpRequest, pk: int, slug: str) -> HttpResponse:
    exercise = get_object_or_404(Exercise, pk=pk, slug=slug)

    context = {'exercise': exercise}

    return render(request, 'exercise/exercise-details.html', context)