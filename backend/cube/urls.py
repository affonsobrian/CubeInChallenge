from django.urls import path, include
from .views import RankView, cube_solver, GenerateCubeView, MovementCubeView, CubeSolverInstanceView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('rank', RankView)
router.register('generatecube', GenerateCubeView)
router.register('movementcube', MovementCubeView)
router.register('solvecube', CubeSolverInstanceView)

urlpatterns = [
    path('', include(router.urls)),
    path('solve/', cube_solver)
]
