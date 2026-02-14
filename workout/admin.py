from django.contrib import admin

from workout.models import WorkoutPlan, WorkoutExercise


# Register your models here.

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1
    ordering = ('order',)


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes')
    list_filter = ('name', 'items__exercise__name')
    search_fields = ('name',)
    inlines = [WorkoutExerciseInline]

