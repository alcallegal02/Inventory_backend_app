# usuarios/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioInternoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioInternoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]