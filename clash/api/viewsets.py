from rest_framework import viewsets
from clash.api import serializers
from clash import models
from rest_framework.permissions import IsAuthenticated

class heroesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.heroesSerializer
    queryset= models.heroes.objects.all()
    permission_classes= (IsAuthenticated,)