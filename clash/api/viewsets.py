from rest_framework import viewsets
from clash.api import serializers
from clash import models
from rest_framework.permissions import IsAuthenticated

class AvatarheroesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AvatarheroesSerializer
    queryset= models.Avatarheroes.objects.all()
    permission_classes= (IsAuthenticated,)


class HeroinaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.HeroinaSerializer
    queryset= models.Heroina.objects.all()
    permission_classes= (IsAuthenticated,)


class KingViewset(viewsets.ModelViewSet):
    serializer_class = serializers.HeroinaSerializer
    queryset= models.King.objects.all()
    permission_classes= (IsAuthenticated,)

class QuennViewset(viewsets.ModelViewSet):
    serializer_class = serializers.QuennSerializer
    queryset= models.Quenn.objects.all()
    permission_classes= (IsAuthenticated,)


class WardenViewset(viewsets.ModelViewSet):
    serializer_class = serializers.WardenSerializer
    queryset= models.Warden.objects.all()
    permission_classes= (IsAuthenticated,)




