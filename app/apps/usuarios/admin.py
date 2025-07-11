# apps/usuarios/admin.py
from django.contrib import admin
from .models import UsuarioInterno

@admin.register(UsuarioInterno)
class UsuarioInternoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellidos', 'email', 'telefono', 'responsable', 'lista_softwares')
    search_fields = ('usuario', 'nombre', 'apellidos', 'email')
    list_filter = ('responsable',)

    def lista_softwares(self, obj):
        return ", ".join([s.nombre for s in obj.softwares.all()])
    lista_softwares.short_description = "Softwares"
