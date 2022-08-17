from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from WebApp.models import Productos, Empleado, Cliente

############################## Menu's Principal ##############################

def inicio(request):
    
    return render(request, "index.html")

def about(request):
    
    return render(request, "about.html")

def contact(request):
    
    return render(request, "contact.html")

############################## Productos ##############################

class CrearProducto(CreateView):
    model = Productos
    template_name = 'formProducto.html'
    fields = ['nombre', 'stock', 'precio', 'Foto']
    success_url = '/webapp/listaProductos'


class BusquedaProducto(ListView):
    template_name = 'busquedaProductos.html'
    model = Productos

    def get_queryset(self):
        print("Ingresando a la funcion busqueda....")
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
            print("Object_list: ", object_list)
        else:
            object_list = self.model.objects.none()
        return object_list


class ListarProductos(ListView):
    model = Productos
    template_name = 'listaProductos.html'


class BorrarProducto(DeleteView):
    model = Productos
    template_name = 'eliminarProducto.html'
    fields = ["nombre", "stock"]
    success_url = '/webapp/listaProductos'


class ActualizarProducto(UpdateView):
    model = Productos
    template_name = 'editarProducto.html'
    fields = ('__all__')
    success_url = '/webapp/listaProductos'


############################## Empleados ##############################

class ListarEmpleados(ListView):
    model = Empleado
    template_name = 'listaEmpleados.html'

class CrearEmpleados(CreateView):
    model = Empleado
    template_name = 'formEmpleados.html'
    fields = ['nombre', 'apellido', 'sexo', 'fecha_nacimiento', 'dni', 'email', 'direccion', 'telefono', 'salario', 'puesto', 'horario', 'foto_empleado']
    success_url = '/webapp/listaEmpleados'

class ActualizarEmpleados(UpdateView):
    model = Empleado
    template_name = 'editarEmpleado.html'
    fields = ('__all__')
    success_url = '/webapp/listaEmpleados'

class BusquedaEmpleado(ListView):
    template_name = 'busquedaEmpleado.html'
    model = Empleado

    def get_queryset(self):
        print("Ingresando a la funcion busqueda....")
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
            print("Object_list: ", object_list)
        else:
            object_list = self.model.objects.none()
        return object_list

class BorrarEmpleados(DeleteView):
    model = Empleado
    template_name = 'eliminarEmpleado.html'
    fields = ["nombre", "apellido"]
    success_url = '/webapp/listaEmpleados'

############################## Clientes ##############################

class CrearCliente(CreateView):
    model = Cliente
    template_name = 'formClientes.html'
    fields = ['nombre', 'apellido', 'nombre_usuario', 'sexo', 'fecha_nacimiento', 'dni', 'email', 'direccion', 'telefono', 'foto_cliente']
    success_url = '/webapp/listaClientes' 

class BusquedaCliente(ListView):
    template_name = 'busquedaCliente.html'
    model = Cliente

    def get_queryset(self):
        print("Ingresando a la funcion busqueda....")
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
            print("Object_list: ", object_list)
        else:
            object_list = self.model.objects.none()
        return object_list

class ListarClientes(ListView):
    model = Cliente
    template_name = 'listaClientes.html'

class BorrarCliente(DeleteView):
    model = Cliente
    template_name = 'eliminarCliente.html'
    fields = ["nombre", "apellido"]
    success_url = '/webapp/listaClientes'

class ActualizarCliente(UpdateView):
    model = Cliente
    template_name = 'editarCliente.html'
    fields = ('__all__')
    success_url = '/webapp/listaClientes'

############################## Vistas basadas en clases ##############################