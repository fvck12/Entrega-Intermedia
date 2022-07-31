from django.db import models

# Create your models here.

class Productos(models.Model):
    Nombre = models.CharField(max_length=50)
    Stock = models.IntegerField()
    Precio = models.IntegerField()
    Foto = models.ImageField(upload_to="Productos/", height_field=None, width_field=None, max_length=None)
