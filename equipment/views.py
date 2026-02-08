from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def add_equipment(request: HttpRequest) -> HttpResponse:
    return render(request, 'equipment/add-equipment.html')

def delete_equipment(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'equipment/delete-equipment.html')

def edit_equipment(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'equipment/edit-equipment.html')

def equipment_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'equipment/equipment-list.html')

def equipment_details(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'equipment/equipment-details.html')