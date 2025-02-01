# Generated by Django 5.1.3 on 2025-01-04 00:04

"""
Tercera migracion
de la aplicacion inventarios
"""

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Clase encargada 
    de la migracion
    """

    dependencies = [
        ('inventario', '0002_alter_usuario_id_organizacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimiento',
            name='id_usuario',
        ),
        migrations.AddField(
            model_name='movimiento',
            name='id_organizacion',
            field=models.ForeignKey(null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='inventario.organizacion'),
        ),
    ]
