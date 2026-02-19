from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from equipment.forms import EquipmentCreateForm, EquipmentEditForm, EquipmentSearchForm
from equipment.models import Equipment

MODEL = Equipment

class EquipmentCreateView(CreateView):
    template_name = 'equipment/add-equipment.html'
    model = MODEL
    form_class = EquipmentCreateForm

    def get_success_url(self):
        return reverse('equipment:details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

class EquipmentDeleteView(DeleteView):
    model = MODEL
    template_name = 'equipment/delete-equipment.html'
    context_object_name = 'equipment_item'
    success_url = reverse_lazy('equipment:list')

class EquipmentEditView(UpdateView):
    model = MODEL
    form_class = EquipmentEditForm
    template_name = 'equipment/edit-equipment.html'
    context_object_name = 'equipment_item'

    def get_success_url(self):
        return reverse('equipment:details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

class EquipmentListView(ListView):
    model = MODEL
    context_object_name = 'equipment_items'
    template_name = 'equipment/equipment-list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name','-created')

        form = EquipmentSearchForm(self.request.GET)
        if form.is_valid():
            q = self.request.GET.get('q')
            if q:
                queryset = queryset.filter(name__icontains=q)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = EquipmentSearchForm(self.request.GET)
        context['button_class'] = 'bg-blue-600 hover:bg-blue-700'
        return context

class EquipmentDetailView(DetailView):
    model = MODEL
    template_name = 'equipment/equipment-details.html'
    context_object_name = 'equipment_item'