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
                fecha_nacimiento=data["fecha_nacimiento"], 
                dni=data["dni"], 
                email=data["email"], 
                direccion=data["direccion"], 
                telefono=data["telefono"],
                puesto=data["puesto"],
                foto_empleado=data["foto_empleado"],
            )
            empleados.save()

            return render(request, "index.html")

    else:
        
        formularioEmpleados= FormEmpleado(request.POST) 

    return render(request, "formEmpleados.html", {"formularioEmpleados": formularioEmpleados})

def lista_empleados(request):
    empleados = Empleado.objects.all()

    contexto= {"empleados": empleados}

    return render(request, "listaEmpleados.html", contexto)

def editar_empleado(request, id):

    empleado = Empleado.objects.get(id=id)

    if request.method == "POST":

        formularioEmpleado= FormEmpleado(request.POST, request.FILES)
        
        if formularioEmpleado.is_valid():

            data= formularioEmpleado.cleaned_data

            empleado.nombre=data["nombre"]
            empleado.apellido=data["apellido"]
            empleado.fecha_nacimiento=data["fecha_nacimiento"]
            empleado.dni=data["dni"]
            empleado.email=data["email"]
            empleado.direccion=data["direccion"]
            empleado.telefono=data["telefono"]
            empleado.puesto=data["puesto"]
            empleado.foto_empleado=data["foto_empleado"]

            empleado.save()

            return render(request, "index.html")

    else:
        
        formularioEmpleado= FormProductos(initial={
            "nombre":empleado.nombre,
            "apellido":empleado.apellido,
            "fecha_nacimiento":empleado.fecha_nacimiento,
            "dni":empleado.dni,
            "email":empleado.email,
            "direccion":empleado.direccion,
            "telefono":empleado.telefono,
            "puesto":empleado.puesto,
            "foto_empleado":empleado.foto_empleado,
        })

    return render(request, "editarProducto.html", {"formularioEmpleado": formularioEmpleado, "id": empleado.id})

def eliminar_empleado(request, id):
    
    if request.method=='POST':

        empleado = Empleado.objects.get(id=id)

        empleado.delete()

        empleado = Empleado.objects.all()

        contexto = {"empleado": empleado}

        return render(request, "listaEmpleados.html", contexto)