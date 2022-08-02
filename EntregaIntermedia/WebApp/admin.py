from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Productos, Empleado, Cliente

class EmpleadosAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'sexo', 'fecha_nacimiento', 'dni', 'email', 'direccion', 'telefono', 'salario', 'puesto', 'horario', 'foto_empleado']

class ProductosAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', 'stock', 'precio', 'Foto']

class ClientesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'sexo', 'fecha_nacimiento', 'dni', 'email', 'direccion', 'telefono', 'nombre_usuario', 'foto_cliente']



# Register your models here.
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Empleado, EmpleadosAdmin)
admin.site.register(Cliente, ClientesAdmin)
