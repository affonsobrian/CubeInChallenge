from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rank 
from .serializers import RankSerializer, CubeSerializer
from django_filters.rest_framework import DjangoFilterBackend


class RankView(viewsets.ModelViewSet):
    queryset = Rank.objects.all().order_by("time")
    serializer_class = RankSerializer
    filterset_fields = ('username',)

# class Solution(viewsets.ViewSet):
#    serializer_class = CubeSerializer


@api_view(['POST'])
def cube_solver(request):
    serializer = CubeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data)
