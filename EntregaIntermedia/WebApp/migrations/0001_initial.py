# Generated by Django 4.0.6 on 2022-07-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Stock', models.IntegerField()),
                ('Precio', models.IntegerField()),
                ('Foto', models.ImageField(upload_to='Productos')),
            ],
        ),
    ]
