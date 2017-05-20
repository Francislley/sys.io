from django.db import models

# Create your models here.


class Perfil(models.Model):
    nome = models.CharField(max_length=60)
    cpf = models.IntegerField()
    email = models.CharField(max_length=50)


