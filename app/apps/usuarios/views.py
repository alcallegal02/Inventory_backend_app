# usuarios/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UsuarioInterno
from .serializers import UsuarioInternoSerializer

class UsuarioInternoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioInterno.objects.all()
    serializer_class = UsuarioInternoSerializer
    permission_classes = [IsAuthenticated]

