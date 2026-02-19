from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from exercise.forms import ExerciseCreateForm, ExerciseEditForm, ExerciseSearchForm
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

class ExerciseListView(ListView):
    model = Exercise
    context_object_name = 'exercises'
    template_name = 'exercise/exercise-list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name','-created')

        form = ExerciseSearchForm(self.request.GET)
        if form.is_valid():
            q= self.request.GET.get('q')
            if q:
                queryset = queryset.filter(name__icontains=q)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ExerciseSearchForm(self.request.GET)
        context['button_class'] = 'bg-green-600 hover:bg-green-700'
        return context

def exercise_details(request: HttpRequest, pk: int, slug: str) -> HttpResponse:
    exercise = get_object_or_404(Exercise, pk=pk, slug=slug)

    context = {'exercise': exercise}

    return render(request, 'exercise/exercise-details.html', context)