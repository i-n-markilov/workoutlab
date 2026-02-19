from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from equipment.forms import EquipmentCreateForm, EquipmentEditForm, EquipmentSearchForm
from equipment.models import Equipment


# Create your views here.
def add_equipment(request: HttpRequest) -> HttpResponse:
    form = EquipmentCreateForm(request.POST or None)

    if request.method== 'POST' and form.is_valid():
        form.save()
        return redirect('equipment:list')

    context = {'form': form}

    return render(request, 'equipment/add-equipment.html', context)

def delete_equipment(request: HttpRequest, pk: int, slug: str) -> HttpResponse:
    equipment_item = get_object_or_404(Equipment, pk=pk, slug=slug)
    if request.method == 'POST':
        equipment_item.delete()
        return redirect('equipment:list')

    context = {'equipment_item': equipment_item}

    return render(request, 'equipment/delete-equipment.html', context)

def edit_equipment(request: HttpRequest, pk: int, slug: str) -> HttpResponse:
    equipment_item = get_object_or_404(Equipment, pk=pk, slug=slug)
    form = EquipmentEditForm(request.POST or None, instance=equipment_item)

    if request.method== 'POST' and form.is_valid():
        form.save()
        return redirect('equipment:list')

    context = {'form': form, 'equipment_item':equipment_item}

    return render(request, 'equipment/edit-equipment.html', context)


class EquipmentListView(ListView):
    model = Equipment
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

def equipment_details(request: HttpRequest, pk: int, slug: str) -> HttpResponse:
    equipment_item = get_object_or_404(Equipment, pk=pk, slug=slug)

    context = {'equipment_item': equipment_item}

    return render(request, 'equipment/equipment-details.html', context)