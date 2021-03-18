from rest_framework.viewsets import ModelViewSet
from project.serializers import ProjectSerializer, Project


# Create your views here.


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.filter(parent=None)
    serializer_class = ProjectSerializer
