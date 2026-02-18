from django import forms

from common.forms import NameSearchForm
from exercise.models import Exercise


class ExerciseFormBasic(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Exercise

class ExerciseCreateForm(ExerciseFormBasic):
    class Meta(ExerciseFormBasic.Meta):
        exclude = ['slug', ]
        help_texts = {
            'name': 'Add exercise name',
            'difficulty': 'Choose an appropriate difficulty',
            'description': 'Add short description',
            'instructions': 'Provide appropriate instructions',
            'primary_muscle_group': 'Select the primary muscle group',
            'secondary_muscle_group': 'Select the secondary muscle group (if applicable)',
            'equipment': 'Select the appropriate equipment (if applicable)',

        }

class ExerciseEditForm(ExerciseFormBasic):
    class Meta(ExerciseFormBasic.Meta):
        widgets = {
            'slug': forms.TextInput(attrs={'disabled': True})
        }

class ExerciseSearchForm(NameSearchForm):
    ...