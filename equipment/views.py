from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from equipment.forms import EquipmentCreateForm, EquipmentEditForm, EquipmentSearchForm
from equipment.models import Equipment

MODEL = Equipment

class EquipmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'equipment/add-equipment.html'
    model = MODEL
    form_class = EquipmentCreateForm

    def get_success_url(self):
        return reverse('equipment:details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EquipmentDeleteView(LoginRequiredMixin, DeleteView):
    model = MODEL
    template_name = 'equipment/delete-equipment.html'
    context_object_name = 'equipment_item'
    success_url = reverse_lazy('equipment:list')

    def get_queryset(self):
        return Equipment.objects.visible_for_user(self.request.user)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'], slug=self.kwargs['slug'])

class EquipmentEditView(LoginRequiredMixin, UpdateView):
    model = MODEL
    form_class = EquipmentEditForm
    template_name = 'equipment/edit-equipment.html'
    context_object_name = 'equipment_item'

    def get_queryset(self):
        return Equipment.objects.visible_for_user(self.request.user)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'], slug=self.kwargs['slug'])

    def get_success_url(self):
        return reverse('equipment:details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

class EquipmentListView(ListView):
    model = MODEL
    context_object_name = 'equipment_items'
    template_name = 'equipment/equipment-list.html'
    paginate_by = 9

    def get_queryset(self):
        qs = Equipment.objects.visible_for_user(self.request.user)
        qs = qs.order_by('name', '-created')

        form = EquipmentSearchForm(self.request.GET)
        if form.is_valid():
            qs = qs.search(form.cleaned_data.get('q'))

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = EquipmentSearchForm(self.request.GET)
        context['button_class'] = 'bg-blue-600 hover:bg-blue-700'
        return context

class EquipmentDetailView(DetailView):
    model = MODEL
    template_name = 'equipment/equipment-details.html'
    context_object_name = 'equipment_item'

    def get_queryset(self):
        return Equipment.objects.visible_for_user(self.request.user)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'], slug=self.kwargs['slug'])