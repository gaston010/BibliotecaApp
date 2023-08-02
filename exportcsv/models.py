from django.db import models


class HistorialForm(models.Model):
    fecha = models.CharField(max_length=20)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20)
