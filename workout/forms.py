from django import forms
from django.forms.models import inlineformset_factory

from workout.models import WorkoutPlan, WorkoutExercise


class WorkoutPlanFormBasic(forms.ModelForm):
    class Meta:
        exclude = ['slug',]
        model = WorkoutPlan

class WorkoutPlanCreateForm(WorkoutPlanFormBasic):
    ...

class WorkoutPlanEditForm(WorkoutPlanFormBasic):
    ...

class WorkoutExerciseForm(forms.ModelForm):
    model = WorkoutExercise

    fields = ['exercise', 'order', 'sets', 'reps', 'duration_seconds', 'rest_seconds' ]

WorkoutExerciseFormSet = inlineformset_factory(
    WorkoutPlan,
    WorkoutExercise,
    exclude=['slug'],
    form = WorkoutExerciseForm,
    extra = 6,
    can_delete = True,
)