from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from workout.forms import WorkoutPlanEditForm, WorkoutPlanCreateForm, dynamic_workout_formset, WorkoutPlanSearchForm
from workout.models import WorkoutPlan


# Create your views here.
def add_workout(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        workout_form = WorkoutPlanCreateForm(request.POST)
        formset_class = dynamic_workout_formset()
        formset = formset_class(request.POST)

        if workout_form.is_valid() and formset.is_valid():
            workout= workout_form.save()
            formset.instance = workout
            formset.save()
            return redirect('workout:list')

    else:
        workout_form = WorkoutPlanCreateForm()
        formset_class = dynamic_workout_formset()
        formset = formset_class()

    context = {'workout_form': workout_form, 'formset': formset}

    return render(request, 'workout/add-workout.html', context)

def delete_workout(request: HttpRequest, pk: int, slug:str) -> HttpResponse:
    workout_plan = get_object_or_404(WorkoutPlan,pk=pk, slug=slug)

    if request.method == "POST":
        workout_plan.delete()
        return redirect('workout:list')

    context = {'workout_plan': workout_plan}

    return render(request, 'workout/delete-workout.html', context)

def edit_workout(request: HttpRequest, pk: int, slug:str) -> HttpResponse:
    workout_plan = get_object_or_404(WorkoutPlan, pk=pk, slug=slug)
    formset_class = dynamic_workout_formset(workout_plan)


    if request.method == "POST":
        workout_form = WorkoutPlanEditForm(request.POST, instance=workout_plan)
        formset = formset_class(request.POST)

        if workout_form.is_valid() and formset.is_valid():
            workout = workout_form.save()
            formset.instance = workout
            formset.save()
            return redirect('workout:list')
    else:
        workout_form = WorkoutPlanEditForm(instance=workout_plan)
        formset = formset_class(instance=workout_plan)

    context = {
        'workout_form': workout_form, 'formset': formset, 'workout_plan': workout_plan,
    }

    return render(request, 'workout/edit-workout.html', context)

def workout_list(request: HttpRequest) -> HttpResponse:
    search_form = WorkoutPlanSearchForm(request.GET or None)

    workout_plans = WorkoutPlan.objects.all()

    if request.GET:
        if search_form.is_valid():
            workout_plans = workout_plans.filter(name__contains=search_form.cleaned_data['query'])

    context = {'workout_plans': workout_plans,
               'search_form': search_form}

    return render(request, 'workout/workout-list.html', context)

def workout_details(request: HttpRequest, pk: int, slug:str) -> HttpResponse:
    workout_plan = get_object_or_404(WorkoutPlan, pk=pk, slug=slug)

    context = {'workout_plan': workout_plan}

    return render(request, 'workout/workout-details.html', context)