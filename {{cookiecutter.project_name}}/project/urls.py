from rest_framework.routers import DefaultRouter
from django.urls import path, include
from project.views import ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
