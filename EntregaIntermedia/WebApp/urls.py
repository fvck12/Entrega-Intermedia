from django.urls import path
from WebApp.views import inicio, about, contact, formularioProductos, busquedaProductos, buscar, lista_productos, eliminar_producto, editar_producto, formularioEmpleados

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
]