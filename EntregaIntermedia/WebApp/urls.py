from django.urls import path
from WebApp.views import inicio, about, productos, contact, formularioProductos, busquedaProductos, buscar, lista_productos

urlpatterns = [
    path('', inicio, name="inicio"),
    path('about', about, name="about"),
    path('contact/', contact, name="contact"),
    path('productos/', productos, name="productos"),    
    path('formProductos/', formularioProductos, name="formProductos"),
    path('busquedaProductos/', busquedaProductos, name="busquedaProductos"),
    path('buscar/', buscar, name="buscar"),
    path('listaProductos/', lista_productos, name="listaProductos"),
]