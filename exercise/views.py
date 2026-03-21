from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from exercise.forms import ExerciseCreateForm, ExerciseEditForm, ExerciseSearchForm
from exercise.models import Exercise

MODEL = Exercise

class ExerciseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'exercise/add-exercise.html'
    model = MODEL
    form_class = ExerciseCreateForm

    def get_success_url(self):
        return reverse('exercise:details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = MODEL
    template_name = 'exercise/delete-exercise.html'
    context_object_name = 'exercise'
    success_url = reverse_lazy('exercise:list')

    def get_queryset(self):
        return Exercise.objects.owned_by(self.request.user)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'], slug=self.kwargs['slug'])

class ExerciseEditView(LoginRequiredMixin, UpdateView):
    model = MODEL
    form_class = ExerciseEditForm
    template_name = 'exercise/edit-exercise.html'
    context_object_name = 'exercise'

    def get_success_url(self):
        return reverse('exercise:details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Exercise.objects.owned_by(self.request.user)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'], slug=self.kwargs['slug'])

class ExerciseListView(ListView):
    model = MODEL
    context_object_name = 'exercises'
    template_name = 'exercise/exercise-list.html'
    paginate_by = 9

    def get_queryset(self):
        qs = Exercise.objects.visible_for_user(self.request.user)
        qs = qs.order_by('name', '-created')

        form = ExerciseSearchForm(self.request.GET)
        if form.is_valid():
            qs = qs.search(form.cleaned_data.get('q'))

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ExerciseSearchForm(self.request.GET)
        context['button_class'] = 'bg-green-600 hover:bg-green-700'
        return context

class ExerciseDetailView(DetailView):
    model = MODEL
    template_name = 'exercise/exercise-details.html'
    context_object_name = 'exercise'

    def get_queryset(self):
        return Exercise.objects.owned_by(self.request.user)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'], slug=self.kwargs['slug'])