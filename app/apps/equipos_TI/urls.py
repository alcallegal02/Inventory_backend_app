# apps/equipos_TI/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PCViewSet,
    PortatilViewSet,
    MonitorViewSet,
    TecladoViewSet,
    RatonViewSet,
    ImpresoraViewSet,
    ImpresoraEtiquetasViewSet,
    SwitchViewSet,
    RouterViewSet,
    OtroViewSet,
    TodosEquiposViewSet
)

router = DefaultRouter()
router.register(r'pcs', PCViewSet)
router.register(r'portatiles', PortatilViewSet)
router.register(r'monitores', MonitorViewSet)
router.register(r'teclados', TecladoViewSet)
router.register(r'ratones', RatonViewSet)
router.register(r'impresoras', ImpresoraViewSet)
router.register(r'impresoras-etiquetas', ImpresoraEtiquetasViewSet)
router.register(r'switches', SwitchViewSet)
router.register(r'routers', RouterViewSet)
router.register(r'otros', OtroViewSet)

# Endpoint especial para todos los equipos
router.register(r'todos', TodosEquiposViewSet, basename='todos-equipos')

urlpatterns = router.urls