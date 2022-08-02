from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from WebApp.models import Productos, Empleado, Persona
from WebApp.forms import FormProductos, FormEmpleado

# Create your views here.

def inicio(request):
    
    return render(request, "index.html")


def about(request):
    
    return render(request, "about.html")


def contact(request):
    
    return render(request, "contact.html")


def formularioProductos(request):

    if request.method == "POST":

        formularioProductos= FormProductos(request.POST, request.FILES)
        
        if formularioProductos.is_valid():

            data= formularioProductos.cleaned_data

            productos = Productos(nombre=data["Nombre"], stock=data["Stock"], precio=data["Precio"], Foto=data["Foto"])
            productos.save()

            return render(request, "index.html")

    else:
        
        formularioProductos= FormProductos(request.POST) 

    return render(request, "formProductos.html", {"formularioProductos": formularioProductos})


def busquedaProductos(request):

    return render(request, "busquedaProducto.html")


def buscar(request):

    if request.GET["Nombre"]:

        nombre= request.GET["Nombre"]

        productos = Productos.objects.filter(Nombre__icontains=nombre)

        return render(request, "resultadoBusqueda.html", {"productos": productos, "Nombre": nombre})
    
    else:

        respuesta= "No enviaste datos"



    return HttpResponse(respuesta)


def lista_productos(request):
    productos = Productos.objects.all()

    contexto= {"productos": productos}

    return render(request, "listaProductos.html", contexto)


def eliminar_producto(request, id):
    
    if request.method=='POST':

        productos = Productos.objects.get(id=id)

        productos.delete()

        productos = Productos.objects.all()

        contexto= {"productos": productos}

        return render(request, "listaProductos.html", contexto)
        

def editar_producto(request, id):

    productos = Productos.objects.get(id=id)

    if request.method == "POST":

        formularioProductos= FormProductos(request.POST, request.FILES)
        
        if formularioProductos.is_valid():

            data= formularioProductos.cleaned_data

            productos.nombre=data["Nombre"]
            productos.stock=data["Stock"] 
            productos.precio=data["Precio"]
            productos.Foto=data["Foto"]

            productos.save()

            return render(request, "index.html")

    else:
        
        formularioProductos= FormProductos(initial={
            "Nombre":productos.nombre,
            "Stock":productos.stock,
            "Precio":productos.precio,
            "Foto":productos.Foto,
        })

    return render(request, "editarProducto.html", {"formularioProductos": formularioProductos, "id": productos.id})


def formularioEmpleados(request):

    if request.method == "POST":

        formularioEmpleados = FormEmpleado(request.POST, request.FILES)
        
        if formularioEmpleados.is_valid():

            data = formularioEmpleados.cleaned_data

            empleados = Empleado(
                nombre=data["nombre"], 
                apellido=data["apellido"], 
                sexo=data["sexo"],
                fecha_nacimiento=data["fecha_nacimiento"], 
                dni=data["dni"], 
                email=data["email"], 
                direccion=data["direccion"], 
                telefono=data["telefono"],
                puesto=data["puesto"],
                horario=data["horario"],
                foto_empleado=data["foto_empleado"],
            )
            empleados.save()

            return render(request, "index.html")

    else:
        
        formularioEmpleados= FormEmpleado(request.POST) 

    return render(request, "formEmpleados.html", {"formularioEmpleados": formularioEmpleados})
