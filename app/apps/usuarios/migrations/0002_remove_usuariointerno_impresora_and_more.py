# Generated by Django 5.2.4 on 2025-07-11 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariointerno',
            name='impresora',
        ),
        migrations.RemoveField(
            model_name='usuariointerno',
            name='impresora_etiquetas',
        ),
        migrations.RemoveField(
            model_name='usuariointerno',
            name='monitor',
        ),
        migrations.RemoveField(
            model_name='usuariointerno',
            name='otro',
        ),
        migrations.RemoveField(
            model_name='usuariointerno',
            name='pc',
        ),
        migrations.RemoveField(
            model_name='usuariointerno',
            name='portatil',
        ),
        migrations.RemoveField(
            model_name='usuariointerno',
            name='raton',
        ),
        migrations.RemoveField(
            model_name='usuariointerno',
            name='router',
        ),
        migrations.RemoveField(
            model_name='usuariointerno',
            name='switch',
        ),
        migrations.RemoveField(
            model_name='usuariointerno',
            name='teclado',
        ),
    ]
