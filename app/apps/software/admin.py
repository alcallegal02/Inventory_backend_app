from django.contrib import admin
from .models import Software

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
