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

# def formularioProductos(request):

#     if request.method == "POST":

#         formularioProductos= FormProductos(request.POST, request.FILES)
        
#         if formularioProductos.is_valid():

#             data= formularioProductos.cleaned_data

#             productos = Productos(nombre=data["nombre"], stock=data["stock"], precio=data["precio"], Foto=data["Foto"])
#             productos.save()

#             return render(request, "index.html")

#     else:
        
#         formularioProductos= FormProductos(request.POST) 

#     return render(request, "formProductos.html", {"formularioProductos": formularioProductos})

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

# def busquedaProductos(request):

#     return render(request, "busquedaProducto.html")

# def buscar(request):

#     if request.GET["nombre"]:

#         nombre= request.GET["nombre"]

#         productos = Productos.objects.filter(nombre__icontains=nombre)

#         return render(request, "resultadoBusqueda.html", {"productos": productos, "nombre": nombre})
    
#     else:

#         respuesta= "No enviaste datos"



#     return HttpResponse(respuesta)


class ListarProductos(ListView):
    model = Productos
    template_name = 'listaProductos.html'


# def lista_productos(request):
#     productos = Productos.objects.all()

#     contexto= {"productos": productos}

#     return render(request, "listaProductos.html", contexto)

class BorrarProducto(DeleteView):
    model = Productos
    template_name = 'eliminarProducto.html'
    fields = ["nombre", "stock"]
    success_url = '/webapp/listaProductos'

# def eliminar_producto(request, id):
    
#     if request.method=='POST':

#         productos = Productos.objects.get(id=id)

#         productos.delete()

#         productos = Productos.objects.all()

#         contexto= {"productos": productos}

#         return render(request, "listaProductos.html", contexto)

class ActualizarProducto(UpdateView):
    model = Productos
    template_name = 'editarProducto.html'
    fields = ('__all__')
    success_url = '/webapp/listaProductos'
        
# def editar_producto(request, id):

#     productos = Productos.objects.get(id=id)

#     if request.method == "POST":

#         formularioProductos= FormProductos(request.POST, request.FILES)
        
#         if formularioProductos.is_valid():

#             data= formularioProductos.cleaned_data

#             productos.nombre=data["nombre"]
#             productos.stock=data["stock"] 
#             productos.precio=data["precio"]
#             productos.Foto=data["Foto"]

#             productos.save()

#             return render(request, "index.html")

#     else:
        
#         formularioProductos= FormProductos(initial={
#             "nombre":productos.nombre,
#             "stock":productos.stock,
#             "precio":productos.precio,
#             "Foto":productos.Foto,
#         })

#     return render(request, "editarProducto.html", {"formularioProductos": formularioProductos, "id": productos.id})

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
    template_name = 'resultadoBusqueda_cliente.html'
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