# Generated by Django 4.2.5 on 2023-11-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.IntegerField(verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='dni',
            field=models.IntegerField(verbose_name='DNI'),
        ),
    ]
