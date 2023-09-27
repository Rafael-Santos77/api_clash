from rest_framework import serializers
from clash import models




class heroesSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.heroes
        fields= '__all__'