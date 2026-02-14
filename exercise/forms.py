from django import forms

from exercise.models import Exercise


class ExerciseFormBasic(forms.ModelForm):
    class Meta:
        exclude = ['slug',]
        model = Exercise

class ExerciseCreateForm(ExerciseFormBasic):
    ...

class ExerciseEditForm(ExerciseFormBasic):
    ...

class ExerciseDeleteForm(ExerciseFormBasic):
    ...