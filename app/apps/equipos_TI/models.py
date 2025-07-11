# inventario/models.py
from django.db import models

class EquipoBase(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    cuota_unidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numero_articulo = models.CharField(max_length=100, null=True, blank=True)
    numero_venta = models.CharField(max_length=100, null=True, blank=True)
    fecha_alta = models.DateField(null=True, blank=True)
    fecha_prevista_baja = models.DateField(null=True, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre} ({self.marca})"


class PC(EquipoBase):
    ip = models.GenericIPAddressField(null=True, blank=True)


class Portatil(EquipoBase):
    ip = models.GenericIPAddressField(null=True, blank=True)


class Monitor(EquipoBase):
    dimensiones = models.CharField(max_length=100, null=True, blank=True)
    puertos = models.CharField(max_length=100, null=True, blank=True)


class Teclado(EquipoBase):
    pass


class Raton(EquipoBase):
    pass


class Impresora(EquipoBase):
    ip = models.GenericIPAddressField(null=True, blank=True)
    controlador = models.CharField(max_length=100, null=True, blank=True)


class ImpresoraEtiquetas(EquipoBase):
    ip = models.GenericIPAddressField(null=True, blank=True)
    controlador = models.CharField(max_length=100, null=True, blank=True)


class Switch(EquipoBase):
    ip = models.GenericIPAddressField(null=True, blank=True)


class Router(EquipoBase):
    ip = models.GenericIPAddressField(null=True, blank=True)


class Otro(EquipoBase):
    ip = models.GenericIPAddressField(null=True, blank=True)
    dimensiones = models.CharField(max_length=100, null=True, blank=True)
    puertos = models.CharField(max_length=100, null=True, blank=True)
    controlador = models.CharField(max_length=100, null=True, blank=True)
