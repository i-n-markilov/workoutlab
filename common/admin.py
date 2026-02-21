from django.contrib import admin

from common.models import MotivationMessage


# Register your models here.
@admin.register(MotivationMessage)
class MotivationMessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'active')
    search_fields = ('text',)
    list_filter = ('active',)
