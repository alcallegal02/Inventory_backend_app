# usuarios/serializers.py
from rest_framework import serializers
from .models import UsuarioInterno
from apps.software.models import Software


class UsuarioInternoSerializer(serializers.ModelSerializer):
    # Usamos un campo SerializerMethodField para evitar el import directo
    softwares = serializers.SerializerMethodField()

    class Meta:
        model = UsuarioInterno
        fields = '__all__'

    def get_softwares(self, obj):
        from apps.software.serializers import SoftwareSerializer  # Import diferido
        return SoftwareSerializer(obj.softwares.all(), many=True).data
