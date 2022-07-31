from django.urls import path

from WebApp.views import inicio, about, productos, contact, formularioProductos, busquedaProductos, buscar

urlpatterns = [
    path('', inicio, name="inicio"),
    path('about', about, name="about"),
    path('productos/', productos, name="productos"),
    path('contact/', contact, name="contact"),
    path('formProductos/', formularioProductos, name="formProductos"),
    path('busquedaProductos/', busquedaProductos, name="busquedaProductos"),
    path('buscar/', buscar, name="buscar"),

]