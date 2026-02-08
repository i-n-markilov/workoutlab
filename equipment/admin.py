from django.contrib import admin

from equipment.models import Equipment


@admin.register(Equipment)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description')
    list_filter = ('name', 'type')
    search_fields = ('name', 'type')