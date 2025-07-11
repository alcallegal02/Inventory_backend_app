# inventario/serializers.py
from rest_framework import serializers
from .models import *


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = '__all__'

class PortatilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portatil
        fields = '__all__'

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'

class TecladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teclado
        fields = '__all__'

class RatonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raton
        fields = '__all__'

class ImpresoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impresora
        fields = '__all__'

class ImpresoraEtiquetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpresoraEtiquetas
        fields = '__all__'

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = '__all__'

class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = '__all__'

class OtroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otro
        fields = '__all__'
