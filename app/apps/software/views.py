from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Software
from .serializers import SoftwareSerializer

class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    permission_classes = [IsAuthenticated]
