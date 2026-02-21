from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from equipment.models import Equipment
from exercise.models import Exercise
from workout.models import WorkoutPlan


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    last_equipment = Equipment.objects.all().order_by('-created').first() or None
    last_exercise = Exercise.objects.all().order_by('-created').first() or None
    last_workout_plan = WorkoutPlan.objects.all().order_by('-created').first() or None

    context = {'last_equipment': last_equipment,
               'last_exercise': last_exercise,
               'last_workout_plan': last_workout_plan}

    return render(request, 'common/home-page.html', context)

