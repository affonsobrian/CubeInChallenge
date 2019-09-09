from rest_framework import serializers
from .models import Rank, Cube
from rubik_solver import utils as rubik_utils
from rubik_solver.Move import Move

ALLOWED_MOVEMENTS = ("F", "L", "R", "B", "U", "D", "F'", "L'",
                     "R'", "B'", "U'", "D'", "F2", "L2", "R2", "B2", "U2", "D2")


class RankSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()

    class Meta:
        model = Rank
        fields = ('id', 'username', 'time', 'position')

    def get_position(self, obj):
        return obj.get_rank_position()


class CubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cube
        fields = ('key', 'positions')
        read_only_fields = ('key', 'positions')

    def create(self, validated_data):
        return Cube.objects.create()


class MovementSerializer(serializers.ModelSerializer):
    movement = serializers.ListField(
        required=True, write_only=True, child=serializers.CharField(max_length=2))

    class Meta:
        model = Cube
        fields = ('key', 'movement', 'positions')
        read_only_fields = ('key', 'positions',)

    def validate_movement(self, movement):
        for m in movement:
            if m not in ALLOWED_MOVEMENTS:
                raise serializers.ValidationError(
                    f"{m} is not a valid movement")
        return movement

    def update(self, instance, validated_data):
        movement = validated_data['movement']
        instance.execute_command(movement)
        return instance


class CubeSolverSerializer(serializers.Serializer):
    positions = serializers.CharField(
        min_length=54, max_length=54, required=True)
    solution = serializers.CharField(read_only=True, default='')

    def validate(self, data):
        data['solution'] = rubik_utils.solve(
            data.get('positions', ''), 'Kociemba')
        return data


class CubeSolverInstanceSerializer(serializers.ModelSerializer):
    solution = serializers.SerializerMethodField()

    class Meta:
        model = Cube
        fields = ('key', 'positions', 'solution')
        read_only_fields = ('key', 'positions', 'solution')

    def get_solution(self, obj):
        return obj.get_solution_list()
