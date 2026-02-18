from email.policy import default

from django import forms

from common.forms import NameSearchForm
from equipment.models import Equipment


class EquipmentFormBasic(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Equipment

class EquipmentCreateForm(EquipmentFormBasic):
    class Meta(EquipmentFormBasic.Meta):
        exclude = ['slug', ]
        help_texts = {
            'name': 'Add equipment name',
            'description': 'Add short description',
            'image_url': 'Equipment image url',
            'type': 'Select the type of equipment',
        }



class EquipmentEditForm(EquipmentFormBasic):
    class Meta(EquipmentFormBasic.Meta):
        widgets = {
            'slug': forms.TextInput(attrs={'disabled': True})
        }


class EquipmentSearchForm(NameSearchForm):
    ...