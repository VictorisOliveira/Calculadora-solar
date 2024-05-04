from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class CalculoSolar(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_calculo = models.DateTimeField(auto_now_add=True)
    ene_kwh = models.FloatField()
    ene_consumo = models.FloatField()
    hs = models.IntegerField()
    sis_solar = models.FloatField()
    inv3 = models.FloatField()
    prod = models.FloatField()
    eco2 = models.FloatField()

    def __str__(self):
        return f"CalculoSolar de {self.usuario.nome} em {self.data_calculo}"

# Create your models here.
