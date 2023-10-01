from rest_framework import serializers
from clash import models




class KingSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.King
        fields= '__all__'


class QuennSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Quenn
        fields= '__all__'


class WardenSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Warden
        fields= '__all__'


class HeroinaSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Heroina
        fields= '__all__'        