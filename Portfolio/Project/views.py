from rest_framework import viewsets
from Project.models import Project
from Project.serializers import ProjectSerializer


class ProjectViewset(viewsets.ModelViewSet):
    """
    Project viewset to help out with only the GET method. It can give you the list of
    Projects or you can retrieve individual Projects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
