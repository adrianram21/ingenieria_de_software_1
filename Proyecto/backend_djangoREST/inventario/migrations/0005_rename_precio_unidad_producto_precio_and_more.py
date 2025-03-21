# Generated by Django 5.1.3 on 2025-02-17 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_precios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio_unidad',
            new_name='precio',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id_organizacion',
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock_minimo',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
