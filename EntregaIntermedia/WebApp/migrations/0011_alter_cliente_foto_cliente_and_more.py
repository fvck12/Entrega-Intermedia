# Generated by Django 4.1 on 2022-08-12 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0010_alter_productos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto_cliente',
            field=models.ImageField(blank=True, null=True, upload_to='Clientes/'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='foto_empleado',
            field=models.ImageField(blank=True, null=True, upload_to='Empleados/'),
        ),
    ]