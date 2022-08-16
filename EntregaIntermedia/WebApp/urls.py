from django.urls import path
from WebApp.views import inicio, about, contact 
from WebApp.views import formularioClientes, busquedaCliente, buscarCliente, lista_clientes, eliminar_cliente, editar_cliente
from WebApp.views import CrearProducto, ListarProductos, BusquedaProducto, BorrarProducto, ActualizarProducto
from WebApp.views import ListarEmpleados, CrearEmpleados, BusquedaEmpleado, BorrarEmpleados, ActualizarEmpleados 

urlpatterns = [
    path('', inicio, name="inicio"),
    path('about', about, name="about"),
    path('contact/', contact, name="contact"),

    path('formProductos/', CrearProducto.as_view(), name="CrearProductos"),
    path('busquedaProductos/', BusquedaProducto.as_view(), name="busquedaProductos"),
    path('listaProductos/', ListarProductos.as_view(), name="listaProductos"),
    path('eliminarProducto/<int:id>', BorrarProducto.as_view(), name="eliminarProducto"),
    path('editarProducto/<int:id>', ActualizarProducto.as_view(), name="editarProducto"),

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