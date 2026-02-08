from django import forms

from equipment.models import Equipment


class EquipmentFormBasic(forms.ModelForm):
    class Meta:
        exclude = ['slug',]
        model = Equipment

class EquipmentCreateForm(EquipmentFormBasic):
    ...

class EquipmentEditForm(EquipmentFormBasic):
    ...

class EquipmentDeleteForm(EquipmentFormBasic):
    ...