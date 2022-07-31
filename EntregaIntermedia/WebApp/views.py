from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from WebApp.models import Productos
from WebApp.forms import FormProductos

# Create your views here.

def inicio(request):
    
    return render(request, "index.html")

def about(request):
    
    return render(request, "about.html")

def productos(request):
    
    return render(request, "productos.html")

def contact(request):
    
    return render(request, "contact.html")

def formularioProductos(request):
    
    

    if request.method == "POST":

        formularioProductos= FormProductos(request.POST, request.FILES)
        
        if formularioProductos.is_valid():

            data= formularioProductos.cleaned_data

            productos = Productos(Nombre=data["Nombre"], Stock=data["Stock"], Precio=data["Precio"], Foto=data["Foto"])
            productos.save()

            return render(request, "index.html")

    else:
        
        formularioProductos= FormProductos(request.POST) 

    return render(request, "formProductos.html", {"formularioProductos": formularioProductos})


def busquedaProductos(request):

    return render(request, "busquedaProducto.html")

def buscar(request):

    if request.GET["Nombre"]:

        Nombre= request.GET["Nombre"]

        productos = Productos.objects.filter(Nombre__icontains=Nombre)

        return render(request, "resultadoBusqueda.html", {"productos": productos, "Nombre": Nombre})
    
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

            productos.Nombre=data["Nombre"]
            productos.Stock=data["Stock"] 
            productos.Precio=data["Precio"]
            productos.Foto=data["Foto"]

            productos.save()

            return render(request, "index.html")

    else:
        
        formularioProductos= FormProductos(initial={
            "Nombre":productos.Nombre,
            "Stock":productos.Stock,
            "Precio":productos.Precio,
            "Foto":productos.Foto,
        })

    return render(request, "editarProducto.html", {"formularioProductos": formularioProductos, "id": productos.id})




