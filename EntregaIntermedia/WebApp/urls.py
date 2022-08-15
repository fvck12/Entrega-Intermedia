from django.urls import path
from WebApp.views import inicio, about, contact 
from WebApp.views import formularioClientes, busquedaCliente, buscarCliente, lista_clientes, eliminar_cliente, editar_cliente
from WebApp.views import formularioProductos, busquedaProductos, buscar, lista_productos, eliminar_producto, editar_producto
from WebApp.views import ListarEmpleados, CrearEmpleados, BusquedaEmpleado, BorrarEmpleados, ActualizarEmpleados

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

    path('formEmpleado/', CrearEmpleados.as_view(), name="CrearEmpleados"),
    path('listaEmpleados/', ListarEmpleados.as_view(), name="listaEmpleados"),
    path('editarEmpleado/<int:pk>', ActualizarEmpleados.as_view(), name="editarEmpleado"),
    path('borrarEmpleado/<int:pk>', BorrarEmpleados.as_view(), name="borrarEmpleado"),
    path('busquedaEmpleado/', BusquedaEmpleado.as_view(), name="busquedaEmpleado"),

    path('formCliente/', formularioClientes, name="formCliente"),
    path('busquedaCliente/', busquedaCliente, name="busquedaCliente"),
    path('buscarCliente/', buscarCliente, name="buscarCliente"),
    path('listaClientes/', lista_clientes, name="listaClientes"),
    path('editarCliente/<int:id>', editar_cliente, name="editarCliente"),
    path('eliminarCliente/<int:id>', eliminar_cliente, name="eliminarCliente"),
]