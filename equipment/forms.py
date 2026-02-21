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
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }
        error_messages = {
            'name': {
                'unique' : 'Equipment already exists. Try something unique!',
                'required' : 'Give the equipment a name so you can find it later.',
                'max_length' : "That's a long name! Please keep it under 100 characters.",
            }
        }



class EquipmentEditForm(EquipmentFormBasic):
    class Meta(EquipmentFormBasic.Meta):
        widgets = {
            'slug': forms.TextInput(attrs={'disabled': True}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }
        error_messages = {
            'name': {
                'unique' : 'Equipment already exists. Try something unique!',
                'required' : 'Keep the equipment name so you can find it later.',
                'max_length' : "That's a long name! Please keep it under 100 characters.",
            }
        }


class EquipmentSearchForm(NameSearchForm):
    ...