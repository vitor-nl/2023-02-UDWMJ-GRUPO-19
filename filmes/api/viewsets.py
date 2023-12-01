from rest_framework import viewsets
from filmes.api import serializers
from filmes import models

class filmesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.filmesSerializer
    queryset = models.filmes.objects.all()