from django.db import models

# Create your models here.
class Motos(models.Model):
    objects = None
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()

class Compras(models.Model):
    objects = None
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=100)

class Hist(models.Model):
    objects = None
    cpf = models.CharField(max_length=150)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()