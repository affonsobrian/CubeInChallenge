from rest_framework import serializers
from .models import Rank
from rubik_solver import utils as rubik_utils

class RankSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    
    class Meta:
        model = Rank
        fields = ('id', 'username', 'time', 'position')

    def get_position(self, obj):
        return obj.get_rank_position()


class CubeSerializer(serializers.Serializer):
    positions = serializers.CharField(min_length=54, max_length=54, required=True)
    solution = serializers.CharField(read_only=True, default='')

    def validate(self, data):
        data['solution'] = rubik_utils.solve(data.get('positions', ''), 'Kociemba')            
        return data