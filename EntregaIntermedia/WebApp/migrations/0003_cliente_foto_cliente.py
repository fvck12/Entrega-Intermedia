# Generated by Django 4.0.6 on 2022-08-02 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_cliente_empleado_rename_nombre_productos_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto_cliente',
            field=models.ImageField(null=True, upload_to='Clientes/'),
        ),
    ]
