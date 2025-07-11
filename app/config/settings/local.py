from .base import *

# Debug settings
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# Security settings (desarrollo)
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0  # Desactivado en desarrollo
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Database (SQLite para desarrollo)
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

# Debug Toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS = ['127.0.0.1']

# Email (consola para desarrollo)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configuración adicional para desarrollo
DEV_APPS = [
    'django_extensions',
]

INSTALLED_APPS += DEV_APPS

# Logging (verbose para desarrollo)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
]

# Permitir estas IPs adicionales en desarrollo
ALLOWED_IP_BLOCKS += ['172.16.0.0/12']  # Docker u otras redes

# Middleware de IP (configuración flexible)
class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if DEBUG:  # En desarrollo, solo registrar sin bloquear
            print(f"Acceso desde IP: {request.META.get('REMOTE_ADDR')}")
        return self.get_response(request)

MIDDLEWARE += ['config.settings.local.IPRestrictionMiddleware']