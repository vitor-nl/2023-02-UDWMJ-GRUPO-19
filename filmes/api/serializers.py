from rest_framework import serializers
from filmes import models

class filmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.filmes
        fields = '__all__'