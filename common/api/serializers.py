from rest_framework import serializers

from equipment.models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            'id',
            'name',
            'description',
            'image',
            'type',
            'private',
            'system_generated',
            'created',
            'modified',
        ]
        read_only_fields = ['slug', 'system_generated', 'created', 'modified']

    def create(self, validated_data):
        equipment = Equipment(**validated_data)
        equipment.user = self.context['request'].user
        equipment.save()
        return equipment