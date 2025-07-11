# apps/equipos_TI/views.py
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    PC,
    Portatil,
    Monitor,
    Teclado,
    Raton,
    Impresora,
    ImpresoraEtiquetas,
    Switch,
    Router,
    Otro
)
from .serializers import (
    PCSerializer,
    PortatilSerializer,
    MonitorSerializer,
    TecladoSerializer,
    RatonSerializer,
    ImpresoraSerializer,
    ImpresoraEtiquetasSerializer,
    SwitchSerializer,
    RouterSerializer,
    OtroSerializer
)


class PCViewSet(viewsets.ModelViewSet):
    queryset = PC.objects.all()
    serializer_class = PCSerializer
    permission_classes = [IsAuthenticated]


class PortatilViewSet(viewsets.ModelViewSet):
    queryset = Portatil.objects.all()
    serializer_class = PortatilSerializer
    permission_classes = [IsAuthenticated]


class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    permission_classes = [IsAuthenticated]


class TecladoViewSet(viewsets.ModelViewSet):
    queryset = Teclado.objects.all()
    serializer_class = TecladoSerializer
    permission_classes = [IsAuthenticated]


class RatonViewSet(viewsets.ModelViewSet):
    queryset = Raton.objects.all()
    serializer_class = RatonSerializer
    permission_classes = [IsAuthenticated]


class ImpresoraViewSet(viewsets.ModelViewSet):
    queryset = Impresora.objects.all()
    serializer_class = ImpresoraSerializer
    permission_classes = [IsAuthenticated]


class ImpresoraEtiquetasViewSet(viewsets.ModelViewSet):
    queryset = ImpresoraEtiquetas.objects.all()
    serializer_class = ImpresoraEtiquetasSerializer
    permission_classes = [IsAuthenticated]


class SwitchViewSet(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
    permission_classes = [IsAuthenticated]


class RouterViewSet(viewsets.ModelViewSet):
    queryset = Router.objects.all()
    serializer_class = RouterSerializer
    permission_classes = [IsAuthenticated]


class OtroViewSet(viewsets.ModelViewSet):
    queryset = Otro.objects.all()
    serializer_class = OtroSerializer
    permission_classes = [IsAuthenticated]

class TodosEquiposViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]

    EQUIPOS_CONFIG = {
        'pcs': {
            'model': PC,
            'serializer': PCSerializer
        },
        'portatiles': {
            'model': Portatil,
            'serializer': PortatilSerializer
        },
        'monitores': {
            'model': Monitor,
            'serializer': MonitorSerializer
        },
        'teclados': {
            'model': Teclado,
            'serializer': TecladoSerializer
        },
        'ratones': {
            'model': Raton,
            'serializer': RatonSerializer
        },
        'impresoras': {
            'model': Impresora,
            'serializer': ImpresoraSerializer
        },
        'impresoras_etiquetas': {
            'model': ImpresoraEtiquetas,
            'serializer': ImpresoraEtiquetasSerializer
        },
        'switches': {
            'model': Switch,
            'serializer': SwitchSerializer
        },
        'routers': {
            'model': Router,
            'serializer': RouterSerializer
        },
        'otros': {
            'model': Otro,
            'serializer': OtroSerializer
        }
    }

    def list(self, request, *args, **kwargs):
        data_serializada = {}
        
        for tipo, config in self.EQUIPOS_CONFIG.items():
            queryset = config['model'].objects.all()
            serializer = config['serializer'](queryset, many=True)
            data_serializada[tipo] = serializer.data

        return Response(data_serializada)