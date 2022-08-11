from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from WebApp.models import Productos, Empleado, Persona, Cliente
from WebApp.forms import FormProductos, FormEmpleado, FormCliente

#Loguin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

############################## Menu's Principal ##############################

def login_request (request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)


            if user is not None:
                login(request, user)

                return render(request, "webapp/", {"mensaje": f"Bienvenido{usuario}"})
            
            else:

                return render(request, "webapp/", {"mensaje":"Error, datos erroneos"})
            
        else:

                return render(request, "webapp/", {"mensaje": "Erorr, formulario erroneo"})
    
    form = AuthenticationForm()

    return render (request, "login.html", {"form":form})


def registro(request):
    
    if request.method =="POST":

        form = UserCreationForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "webapp/", {"mensaje":"Usuario creado"})

    
    else:
        form = UserCreationForm()

    return render(request, "registro.html", {"form": form})


        


############################## Menu's Principal ##############################

def inicio(request):
    
    return render(request, "index.html")

def about(request):
    
    return render(request, "about.html")

def contact(request):
    
    return render(request, "contact.html")

############################## Productos ##############################

def formularioProductos(request):

    if request.method == "POST":

        formularioProductos= FormProductos(request.POST, request.FILES)
        
        if formularioProductos.is_valid():

            data= formularioProductos.cleaned_data

            productos = Productos(nombre=data["nombre"], stock=data["stock"], precio=data["precio"], Foto=data["Foto"])
            productos.save()

            return render(request, "index.html")

    else:
        
        formularioProductos= FormProductos(request.POST) 

    return render(request, "formProductos.html", {"formularioProductos": formularioProductos})

def busquedaProductos(request):

    return render(request, "busquedaProducto.html")

def buscar(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]

        productos = Productos.objects.filter(nombre__icontains=nombre)

        return render(request, "resultadoBusqueda.html", {"productos": productos, "nombre": nombre})
    
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

            productos.nombre=data["nombre"]
            productos.stock=data["stock"] 
            productos.precio=data["precio"]
            productos.Foto=data["Foto"]

            productos.save()

            return render(request, "index.html")

    else:
        
        formularioProductos= FormProductos(initial={
            "nombre":productos.nombre,
            "stock":productos.stock,
            "precio":productos.precio,
            "Foto":productos.Foto,
        })

    return render(request, "editarProducto.html", {"formularioProductos": formularioProductos, "id": productos.id})

############################## Empleados ##############################

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
                salario=data["salario"],
                horario=data["horario"],
                foto_empleado=data["foto_empleado"],
            )
            empleados.save()

            return render(request, "index.html")

    else:
        
        formularioEmpleados= FormEmpleado(request.POST) 

    return render(request, "formEmpleados.html", {"formularioEmpleados": formularioEmpleados})

def busquedaEmpleado(request):

    return render(request, "busquedaEmpleado.html")

def buscarEmpleado(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]

        empleados = Empleado.objects.filter(nombre__icontains=nombre)

        return render(request, "resultadoBusqueda_empleado.html", {"empleados": empleados, "nombre": nombre})
    
    else:

        respuesta= "No enviaste datos"

    return HttpResponse(respuesta)

def lista_empleados(request):
    empleados = Empleado.objects.all()

    contexto= {"empleados": empleados}

    return render(request, "listaEmpleados.html", contexto)

def eliminar_empleado(request, id):
        
    if request.method=='POST':

        empleado = Empleado.objects.get(id=id)

        empleado.delete()

        empleado = Empleado.objects.all()

        contexto = {"empleado": empleado}

        return render(request, "listaEmpleados.html", contexto)

def editar_empleado(request, id):

    empleado = Empleado.objects.get(id=id)

    if request.method == "POST":

        formularioEmpleados = FormEmpleado(request.POST, request.FILES)
        
        if formularioEmpleados.is_valid():

            data= formularioEmpleados.cleaned_data

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
        
        formularioEmpleados = FormEmpleado(initial={
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

    return render(request, "editarEmpleado.html", {"formularioEmpleados": formularioEmpleados, "id": empleado.id})

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