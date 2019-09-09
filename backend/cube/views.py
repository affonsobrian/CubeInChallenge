from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rank, Cube
from .serializers import RankSerializer, CubeSolverSerializer, CubeSerializer, MovementSerializer, CubeSolverInstanceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet


class RankView(viewsets.ModelViewSet):
    queryset = Rank.objects.all().order_by("time")
    serializer_class = RankSerializer
    filterset_fields = ('username',)


class GenerateCubeView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Cube.objects.all()
    serializer_class = CubeSerializer


class MovementCubeView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Cube.objects.all()
    serializer_class = MovementSerializer


class CubeSolverInstanceView(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Cube.objects.all()
    serializer_class = CubeSolverInstanceSerializer


@api_view(['POST'])
def cube_solver(request):
    serializer = CubeSolverSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data)
