from django.db import models
from apps.usuarios.models import UsuarioInterno

class Software(models.Model):
    nombre = models.CharField(max_length=100)
    usuarios = models.ManyToManyField(UsuarioInterno, related_name='softwares', blank=True)

    def __str__(self):
        return f"{self.nombre}"
