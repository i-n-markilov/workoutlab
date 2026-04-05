from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from common.api.serializers import EquipmentSerializer
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

class ListCreateEquipmentApiView(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)