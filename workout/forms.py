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
        widgets = {
            'notes': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }
        error_messages = {
            'name': {
                'unique' : 'Workout plan already exists. Try something unique!',
                'required' : 'Give the Workout plan a name so you can find it later.',
                'max_length' : "That's a long name! Please keep it under 100 characters.",
            }
        }

class WorkoutPlanEditForm(WorkoutPlanFormBasic):
    class Meta(WorkoutPlanFormBasic.Meta):
        widgets = {
            'slug': forms.TextInput(attrs={'disabled': True}),
            'notes': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }
        error_messages = {
            'name': {
                'unique' : 'Workout plan already exists. Try something unique!',
                'required' : 'Keep the workout plan a name so you can find it later.',
                'max_length' : "That's a long name! Please keep it under 100 characters.",
            }
        }

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'order', 'sets', 'reps', 'duration_seconds', 'rest_seconds']
        labels = {
            'order': 'Order of execution',
            'duration_seconds': 'Duration (sec)',
            'rest_seconds': 'Rest (sec)',
        }



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