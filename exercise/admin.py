from django.contrib import admin

from exercise.models import Exercise


# Register your models here.
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'primary_muscle_group', 'description', 'is_bodyweight')
    list_filter = ('name','difficulty', 'primary_muscle_group', )
    search_fields = ('name',)
    filter_horizontal = ('equipment',)