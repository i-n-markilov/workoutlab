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
            'is_bodyweight': 'Mark if exercise uses only body weight',
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'instructions': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }
        error_messages = {
            'name': {
                'unique' : 'Exercise already exists. Try something unique!',
                'required' : 'Give the Exercise a name so you can find it later.',
                'max_length' : "That's a long name! Please keep it under 100 characters.",
            },
            'primary_muscle_group': {
                'required' : 'Select the main muscle group this exercise targets',
            }

        }

    def clean(self):
        cleaned_data = super().clean()

        primary_muscle_group = cleaned_data.get('primary_muscle_group')
        secondary_muscle_group = cleaned_data.get('secondary_muscle_group')

        if primary_muscle_group and secondary_muscle_group:
            if primary_muscle_group == secondary_muscle_group:
                raise forms.ValidationError('Primary and secondary muscle groups cannot be the same')

        return cleaned_data


class ExerciseEditForm(ExerciseFormBasic):
    class Meta(ExerciseFormBasic.Meta):
        widgets = {
            'slug': forms.TextInput(attrs={'disabled': True}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'instructions': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }
        help_texts = {
            'name': 'Add exercise name',
            'difficulty': 'Choose an appropriate difficulty',
            'description': 'Add short description',
            'instructions': 'Provide appropriate instructions',
            'primary_muscle_group': 'Select the primary muscle group',
            'secondary_muscle_group': 'Select the secondary muscle group (if applicable)',
            'equipment': 'Select the appropriate equipment (if applicable)',
            'is_bodyweight': 'Mark if exercise uses only body weight',
        }
        error_messages = {
            'name': {
                'unique' : 'Exercise already exists. Try something unique!',
                'required' : 'Keep the Exercise name so you can find it later.',
                'max_length' : "That's a long name! Please keep it under 100 characters.",
            }
        }

class ExerciseSearchForm(NameSearchForm):
    ...