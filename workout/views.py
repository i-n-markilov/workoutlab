from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, DeleteView

from workout.forms import WorkoutPlanEditForm, WorkoutPlanCreateForm, dynamic_workout_formset, WorkoutPlanSearchForm
from workout.models import WorkoutPlan

MODEL = WorkoutPlan

@login_required
def add_workout(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        workout_form = WorkoutPlanCreateForm(request.POST)
        if workout_form.is_valid():
            workout = workout_form.save(commit=False)
            workout.user = request.user
            if not workout.slug:
                workout.slug = slugify(workout.name)

            formset = dynamic_workout_formset(instance=workout, user=request.user, data=request.POST)
            if formset.is_valid():
                workout.save()
                formset.save()
                return redirect('workout:details', pk=workout.pk, slug=workout.slug)
        else:
            workout = WorkoutPlan()
            formset = dynamic_workout_formset(instance=workout, user=request.user, data=request.POST)
    else:
        workout_form = WorkoutPlanCreateForm()
        workout = WorkoutPlan()
        formset = dynamic_workout_formset(instance=workout, user=request.user,)

    return render(request, 'workout/add-workout.html', {
        'workout_form': workout_form,
        'formset': formset,
    })

class WorkoutPlanDeleteView(LoginRequiredMixin,DeleteView):
    model = MODEL
    template_name = 'workout/delete-workout.html'
    context_object_name = 'workout_plan'
    success_url = reverse_lazy('workout:list')

@login_required
def edit_workout(request: HttpRequest, pk: int, slug:str) -> HttpResponse:
    workout_plan = get_object_or_404(WorkoutPlan, pk=pk, slug=slug)

    if workout_plan.user != request.user:
        raise PermissionDenied("You can only edit your own workouts!")

    if request.method == "POST":
        workout_form = WorkoutPlanEditForm(request.POST, instance=workout_plan)
        formset = dynamic_workout_formset(instance=workout_plan, user=request.user, data=request.POST)

        if workout_form.is_valid() and formset.is_valid():
            workout_form.save()
            formset.save()
            return redirect('workout:details', pk=workout_plan.pk, slug=workout_plan.slug)
    else:
        workout_form = WorkoutPlanEditForm(instance=workout_plan)
        formset = dynamic_workout_formset(instance=workout_plan, user=request.user,)

    context = {
        'workout_form': workout_form,
        'formset': formset,
        'workout_plan': workout_plan,
    }
    return render(request, 'workout/edit-workout.html', context)

class WorkoutPlanListView(ListView):
    model = MODEL
    context_object_name = 'workout_plans'
    template_name = 'workout/workout-list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name','-created')
        user = self.request.user

        if user.is_authenticated:
            queryset = queryset.filter(Q(private=False) | Q(user=user))
        else:
            queryset = queryset.filter(private=False)


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

class WorkoutPlanDetailView(DetailView):
    model = MODEL
    template_name = 'workout/workout-details.html'
    context_object_name = 'workout_plan'