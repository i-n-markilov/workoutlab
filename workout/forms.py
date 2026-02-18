from django import forms
from django.forms import inlineformset_factory

from common.forms import NameSearchForm
from workout.models import WorkoutPlan, WorkoutExercise


class WorkoutPlanFormBasic(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = WorkoutPlan

class WorkoutPlanCreateForm(WorkoutPlanFormBasic):
    class Meta(WorkoutPlanFormBasic.Meta):
        exclude = ['slug',]
        help_texts = {
            'name': 'Add workout plan name',
            'notes': 'Add some helpful notes',
        }

class WorkoutPlanEditForm(WorkoutPlanFormBasic):
    class Meta(WorkoutPlanFormBasic.Meta):
        widgets = {
            'slug': forms.TextInput(attrs={'disabled': True})
        }

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'order', 'sets', 'reps', 'duration_seconds', 'rest_seconds']



TOTAL_FORMS_COUNT = 6

def dynamic_workout_formset(instance,data=None, total_forms = TOTAL_FORMS_COUNT):
    if instance.pk:
        existing_exercises = instance.items.count()
    else:
        existing_exercises = 0

    extra_forms = max(total_forms - existing_exercises, 0)


    WorkoutExerciseFormSet = inlineformset_factory(
        WorkoutPlan,
        WorkoutExercise,
        form=WorkoutExerciseForm,
        can_delete=True,
        extra=extra_forms,
    )

    return WorkoutExerciseFormSet(data=data, instance=instance)

class WorkoutPlanSearchForm(NameSearchForm):
    ...