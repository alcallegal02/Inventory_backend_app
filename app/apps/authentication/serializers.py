# apps/authentication/serializers.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login, User
from django.utils.translation import gettext_lazy as _

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD  # Usado por TokenObtainPairSerializer

    def validate(self, attrs):
        login_input = attrs.get('username')  # Este puede ser username o email
        password = attrs.get('password')

        # Intentar buscar por username o email
        user_obj = User.objects.filter(username=login_input).first() or User.objects.filter(email=login_input).first()

        if user_obj is None:
            raise serializers.ValidationError(_("Usuario no encontrado."))

        # Autenticamos con el username real y el password
        user = authenticate(username=user_obj.username, password=password)

        if not user:
            raise serializers.ValidationError(_("Credenciales inválidas."))

        self.user = user
        data = super().validate({'username': user.username, 'password': password})

        data['user'] = {
            # 'username': self.user.username,
            # 'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
        }

        update_last_login(None, self.user)
        return data
