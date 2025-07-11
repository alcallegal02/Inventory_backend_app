# apps/equipos_TI/admin.py
from django.contrib import admin
from .models import PC, Portatil, Monitor, Teclado, Raton, Impresora, ImpresoraEtiquetas, Switch, Router, Otro

admin.site.register(PC)
admin.site.register(Portatil)
admin.site.register(Monitor)
admin.site.register(Teclado)
admin.site.register(Raton)
admin.site.register(Impresora)
admin.site.register(ImpresoraEtiquetas)
admin.site.register(Switch)
admin.site.register(Router)
admin.site.register(Otro)
