# apps/equipos_TI/models.py
from django.db import models

ESTADOS_CHOICES = [
    ("asignado", "Asignado a un usuario/equipo"),
    ("almacen_uso", "En almacén para usar"),
    ("almacen_devolucion", "En almacén para devolver"),
]

UBICACIONES_CHOICES = [
    ("almacen_n1", "Almacén N1"),
    ("almacen_n2", "Almacén N2"),
    ("verificacion_n1", "Verificación N1"),
    ("verificacion_n2", "Verificación N2"),
    ("archivo", "Archivo"),
    ("taller", "Taller"),
]

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
    ubicacion = models.CharField(max_length=50, choices=UBICACIONES_CHOICES, default="archivo")
    comentario = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default="almacen_uso")

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
    pc_asociado = models.ForeignKey('PC', null=True, blank=True, on_delete=models.SET_NULL, related_name='monitores')
    portatil_asociado = models.ForeignKey('Portatil', null=True, blank=True, on_delete=models.SET_NULL, related_name='monitores')


class Teclado(EquipoBase):
    pc_asociado = models.ForeignKey('PC', null=True, blank=True, on_delete=models.SET_NULL, related_name='teclados')
    portatil_asociado = models.ForeignKey('Portatil', null=True, blank=True, on_delete=models.SET_NULL, related_name='teclados')


class Raton(EquipoBase):
    pc_asociado = models.ForeignKey('PC', null=True, blank=True, on_delete=models.SET_NULL, related_name='ratones')
    portatil_asociado = models.ForeignKey('Portatil', null=True, blank=True, on_delete=models.SET_NULL, related_name='ratones')


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
