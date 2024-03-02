from . import models 
from . import serializer
from rest_framework import viewsets, permissions

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.ProjecSerializer
