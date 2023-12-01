from django.db import models

class filmes(models.Model):
    nome_filme = models.CharField(primary_key=True, max_length=255)
    criador_filme = models.CharField(max_length=100)
    ano_filme = models.IntegerField()
    criado = models.DateField(auto_now_add=True)
    resumo_filme = models.CharField(max_length=255)