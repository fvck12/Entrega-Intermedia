from django.urls import path
from WebApp.views import inicio, about, contact 
from WebApp.views import CrearProducto, ListarProductos, BusquedaProducto, BorrarProducto, ActualizarProducto
from WebApp.views import ListarEmpleados, CrearEmpleados, BusquedaEmpleado, BorrarEmpleados, ActualizarEmpleados
from WebApp.views import ActualizarCliente, BorrarCliente, BusquedaCliente, CrearCliente, ListarClientes


urlpatterns = [
    path('', inicio, name="inicio"),
    path('about', about, name="about"),
    path('contact/', contact, name="contact"),

    path('formProducto/', CrearProducto.as_view(), name="CrearProductos"),
    path('busquedaProductos/', BusquedaProducto.as_view(), name="busquedaProductos"),
    path('listaProductos/', ListarProductos.as_view(), name="listaProductos"),
    path('eliminarProducto/<int:pk>', BorrarProducto.as_view(), name="eliminarProducto"),
    path('editarProducto/<int:pk>', ActualizarProducto.as_view(), name="editarProducto"),

    path('formEmpleado/', CrearEmpleados.as_view(), name="CrearEmpleados"),
    path('listaEmpleados/', ListarEmpleados.as_view(), name="listaEmpleados"),
    path('editarEmpleado/<int:pk>', ActualizarEmpleados.as_view(), name="editarEmpleado"),
    path('borrarEmpleado/<int:pk>', BorrarEmpleados.as_view(), name="borrarEmpleado"),
    path('busquedaEmpleado/', BusquedaEmpleado.as_view(), name="busquedaEmpleado"),

    path('formCliente/', CrearCliente.as_view(), name="CrearClientes"),
    path('busquedaCliente/', BusquedaCliente.as_view(), name="busquedaCliente"),
    path('listaClientes/', ListarClientes.as_view(), name="listaClientes"),
    path('eliminarCliente/<int:pk>', BorrarCliente.as_view(), name="eliminarCliente"),
    path('editarCliente/<int:pk>', ActualizarCliente.as_view(), name="editarCliente"),

]