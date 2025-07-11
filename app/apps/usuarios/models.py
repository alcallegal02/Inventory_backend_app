from django.db import models


class UsuarioInterno(models.Model):
    usuario = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    responsable = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="subordinados"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.usuario})"
