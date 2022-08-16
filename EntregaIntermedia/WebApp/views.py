from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from WebApp.models import Productos, Empleado, Cliente
from WebApp.forms import FormProductos, FormCliente

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

def formularioClientes(request):

    if request.method == "POST":

        formularioClientes = FormCliente(request.POST, request.FILES)
        
        if formularioClientes.is_valid():

            data = formularioClientes.cleaned_data

            clientes = Cliente( 
                nombre=data["nombre"], 
                apellido=data["apellido"],
                nombre_usuario=data["nombre_usuario"],
                sexo=data["sexo"],
                fecha_nacimiento=data["fecha_nacimiento"], 
                dni=data["dni"], 
                email=data["email"], 
                direccion=data["direccion"], 
                telefono=data["telefono"],
                foto_cliente=data["foto_cliente"],
            )
            clientes.save()

            return render(request, "index.html")

    else:
        
        formularioClientes= FormCliente(request.POST) 

    return render(request, "formClientes.html", {"formularioClientes": formularioClientes})

def busquedaCliente(request):

    return render(request, "busquedaCliente.html")

def buscarCliente(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]

        clientes = Cliente.objects.filter(nombre__icontains=nombre)

        return render(request, "resultadoBusqueda_cliente.html", {"clientes": clientes, "nombre": nombre})
    
    else:

        respuesta= "No enviaste datos"

    return HttpResponse(respuesta)

def lista_clientes(request):
    clientes = Cliente.objects.all()

    contexto= {"clientes": clientes}

    return render(request, "listaClientes.html", contexto)

def eliminar_cliente(request, id):
    
    if request.method=='POST':

        cliente = Cliente.objects.get(id=id)

        cliente.delete()

        cliente = Cliente.objects.all()

        contexto = {"cliente": cliente}

        return render(request, "listaClientes.html", contexto)

def editar_cliente(request, id):

    cliente = Cliente.objects.get(id=id)

    if request.method == "POST":

        formularioClientes= FormCliente(request.POST, request.FILES)
        
        if formularioClientes.is_valid():

            data= formularioClientes.cleaned_data
            
            
            cliente.nombre=data["nombre"]
            cliente.apellido=data["apellido"]
            cliente.fecha_nacimiento=data["fecha_nacimiento"]
            cliente.dni=data["dni"]
            cliente.email=data["email"]
            cliente.direccion=data["direccion"]
            cliente.telefono=data["telefono"]
            cliente.nombre_usuario=data["nombre_usuario"]
            cliente.foto_cliente=data["foto_cliente"]

            cliente.save()

            return render(request, "index.html")

    else:
        
        formularioClientes= FormCliente(initial={
            "nombre":cliente.nombre,
            "apellido":cliente.apellido,
            "fecha_nacimiento":cliente.fecha_nacimiento,
            "dni":cliente.dni,
            "email":cliente.email,
            "direccion":cliente.direccion,
            "telefono":cliente.telefono,
            "nombre_usuario":cliente.nombre_usuario,
            "foto_cliente":cliente.foto_cliente,
        })

    return render(request, "editarCliente.html", {"formularioClientes": formularioClientes, "id": cliente.id})

############################## Vistas basadas en clases ##############################