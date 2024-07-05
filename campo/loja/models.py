from django.db import models
from django.utils import timezone

class Produto(models.Model):

    nome = models.CharField(max_length=100)
    preco = models.IntegerField()

    def __str__(self):
        return self.nome

class Fornecedore(models.Model):
    nome = models.CharField(max_length=200)   

    def __str__(self):
        return self.nome       
# Create your models here.
