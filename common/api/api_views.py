from rest_framework.response import Response
from rest_framework.views import APIView
from equipment.models import Equipment
from exercise.models import Exercise
from workout.models import WorkoutPlan


class StatsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        stats = {
            'equipment_count': Equipment.objects.count(),
            'exercise_count': Exercise.objects.count(),
            'workoutplan_count': WorkoutPlan.objects.count(),
        }

        return Response(stats)