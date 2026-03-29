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

def cloudinary_default_images(request):
    return {
        'CLOUDINARY_404': 'https://res.cloudinary.com/dj9ttpawg/image/upload/v1774791555/404_cqjcp4.png',
        'CLOUDINARY_DEFAULT_EQUIPMENT': 'https://res.cloudinary.com/dj9ttpawg/image/upload/v1774791555/equipment-default_xnq318.png',
        'CLOUDINARY_LOGO': 'https://res.cloudinary.com/dj9ttpawg/image/upload/v1774791556/wl-logo_trv3ig.png',
        'CLOUDINARY_ICON': 'https://res.cloudinary.com/dj9ttpawg/image/upload/v1774791555/wl-icon-no-bg_srrlzq.png'
    }