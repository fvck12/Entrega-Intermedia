from django.urls import path
from WebApp.views import inicio, about, contact, formularioProductos, busquedaProductos, buscar, lista_productos, eliminar_producto, editar_producto, formularioEmpleados, lista_empleados, editar_empleado, eliminar_empleado, editar_cliente, eliminar_cliente, formularioClientes, lista_clientes

urlpatterns = [
    path('', inicio, name="inicio"),
    path('about', about, name="about"),
    path('contact/', contact, name="contact"),        
    path('formProductos/', formularioProductos, name="formProductos"),
    path('busquedaProductos/', busquedaProductos, name="busquedaProductos"),
    path('buscar/', buscar, name="buscar"),
    path('listaProductos/', lista_productos, name="listaProductos"),
    path('eliminarProducto/<int:id>', eliminar_producto, name="eliminarProducto"),
    path('editarProducto/<int:id>', editar_producto, name="editarProducto"),
    path('formEmpleado/', formularioEmpleados, name="formEmpleado"),
    path('listaEmpleados/', lista_empleados, name="listaempleados"),
    path('editarEmpleado/<int:id>', editar_empleado, name="editarEmpleado"),
    path('eliminarEmpleado/<int:id>', eliminar_empleado, name="eliminarEmpleado"),
    path('formCliente/', formularioClientes, name="formCliente"),
    path('listaClientes/', lista_clientes, name="listaclientes"),
    path('editarCliente/<int:id>', editar_cliente, name="editarCliente"),
    path('eliminarCliente/<int:id>', eliminar_cliente, name="eliminarCliente"),
]