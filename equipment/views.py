from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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

def equipment_list(request: HttpRequest) -> HttpResponse:
    search_form = EquipmentSearchForm(request.GET or None)

    equipment_items = Equipment.objects.all().order_by('name', 'created')

    if request.GET:
        if search_form.is_valid():
            equipment_items = equipment_items.filter(name__icontains=search_form.cleaned_data['query'])

    context = {'equipment_items': equipment_items,
               'search_form': search_form}

    return render(request, 'equipment/equipment-list.html', context)

def equipment_details(request: HttpRequest, pk: int, slug: str) -> HttpResponse:
    equipment_item = get_object_or_404(Equipment, pk=pk, slug=slug)

    context = {'equipment_item': equipment_item}

    return render(request, 'equipment/equipment-details.html', context)