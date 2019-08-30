from django.urls import path, include
from .views import RankView, cube_solver
from rest_framework import routers

router = routers.DefaultRouter()
router.register('rank', RankView)

urlpatterns = [
    path('', include(router.urls)),
    path('solve/', cube_solver)
]
