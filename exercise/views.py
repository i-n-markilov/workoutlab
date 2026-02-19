from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from exercise.forms import ExerciseCreateForm, ExerciseEditForm, ExerciseSearchForm
from exercise.models import Exercise

MODEL = Exercise

class ExerciseCreateView(CreateView):
    template_name = 'exercise/add-exercise.html'
    model = MODEL
    form_class = ExerciseCreateForm

    def get_success_url(self):
        return reverse('exercise:details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

class ExerciseDeleteView(DeleteView):
    model = MODEL
    template_name = 'exercise/delete-exercise.html'
    context_object_name = 'exercise'
    success_url = reverse_lazy('exercise:list')

class ExerciseEditView(UpdateView):
    model = MODEL
    form_class = ExerciseEditForm
    template_name = 'exercise/edit-exercise.html'
    context_object_name = 'exercise'

    def get_success_url(self):
        return reverse('exercise:details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

class ExerciseListView(ListView):
    model = MODEL
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

class ExerciseDetailView(DetailView):
    model = MODEL
    template_name = 'exercise/exercise-details.html'
    context_object_name = 'exercise'