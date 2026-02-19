from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView

from workout.forms import WorkoutPlanEditForm, WorkoutPlanCreateForm, dynamic_workout_formset, WorkoutPlanSearchForm
from workout.models import WorkoutPlan


# Create your views here.
def add_workout(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        workout_form = WorkoutPlanCreateForm(request.POST)
        if workout_form.is_valid():
            workout = workout_form.save(commit=False)
            if not workout.slug:
                workout.slug = slugify(workout.name)
            workout.save()

            formset = dynamic_workout_formset(instance=workout, data=request.POST)
            if formset.is_valid():
                formset.save()
                return redirect('workout:details', pk=workout.pk, slug=workout.slug)
        else:
            workout = WorkoutPlan()
            formset = dynamic_workout_formset(instance=workout, data=request.POST)
    else:
        workout_form = WorkoutPlanCreateForm()
        workout = WorkoutPlan()
        formset = dynamic_workout_formset(instance=workout)

    return render(request, 'workout/add-workout.html', {
        'workout_form': workout_form,
        'formset': formset,
    })

def delete_workout(request: HttpRequest, pk: int, slug:str) -> HttpResponse:
    workout_plan = get_object_or_404(WorkoutPlan,pk=pk, slug=slug)

    if request.method == "POST":
        workout_plan.delete()
        return redirect('workout:list')

    context = {'workout_plan': workout_plan}

    return render(request, 'workout/delete-workout.html', context)

def edit_workout(request: HttpRequest, pk: int, slug:str) -> HttpResponse:
    workout_plan = get_object_or_404(WorkoutPlan, pk=pk, slug=slug)

    if request.method == "POST":
        workout_form = WorkoutPlanEditForm(request.POST, instance=workout_plan)
        formset = dynamic_workout_formset(instance=workout_plan, data=request.POST)

        if workout_form.is_valid() and formset.is_valid():
            workout_form.save()
            formset.save()
            return redirect('workout:details', pk=workout_plan.pk, slug=workout_plan.slug)
    else:
        workout_form = WorkoutPlanEditForm(instance=workout_plan)
        formset = dynamic_workout_formset(instance=workout_plan)

    context = {
        'workout_form': workout_form,
        'formset': formset,
        'workout_plan': workout_plan,
    }
    return render(request, 'workout/edit-workout.html', context)

class WorkoutPlanListView(ListView):
    model = WorkoutPlan
    context_object_name = 'workout_plans'
    template_name = 'workout/workout-list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name','-created')

        form = WorkoutPlanSearchForm(self.request.GET)
        if form.is_valid():
            q = self.request.GET.get('q')
            if q:
                queryset = queryset.filter(name__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = WorkoutPlanSearchForm(self.request.GET)
        context['button_class'] = 'bg-purple-600 hover:bg-purple-700'
        return context

def workout_details(request: HttpRequest, pk: int, slug:str) -> HttpResponse:
    workout_plan = get_object_or_404(WorkoutPlan, pk=pk, slug=slug)

    context = {'workout_plan': workout_plan}

    return render(request, 'workout/workout-details.html', context)