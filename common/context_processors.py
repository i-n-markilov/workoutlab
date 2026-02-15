from django.core.cache import cache

from common.models import MotivationMessage
from equipment.models import Equipment
from exercise.models import Exercise
from workout.models import WorkoutPlan


def footer_stats(request):
    counts = {
        "equipment_count": Equipment.objects.count(),
        "exercise_count": Exercise.objects.count(),
        "workout_plan_count": WorkoutPlan.objects.count(),
    }

    return counts

def footer_message(request):
    message = MotivationMessage.objects.filter(active=True).order_by('?').first()

    return {
        "motivation_message": message.text if message else ""
    }