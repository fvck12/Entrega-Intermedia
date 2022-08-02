from django import forms
from WebApp.models import Empleado, Cliente

class FormProductos(forms.Form):

    nombre= forms.CharField()
    stock= forms.IntegerField()
    precio= forms.IntegerField()
    Foto= forms.ImageField()

class FormEmpleado(forms.ModelForm):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.DateField()
    dni = forms.IntegerField()
    email = forms.EmailField()
    direccion = forms.CharField()
    telefono = forms.IntegerField()
    puesto = forms.CharField()
    foto_empleado = forms.ImageField()

    class Meta:
        model = Empleado
        fields = ['sexo', 'horario']
    

class FormCliente(forms.ModelForm):

    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.DateField()
    dni = forms.IntegerField()
    email = forms.EmailField()
    direccion = forms.CharField()
    telefono = forms.IntegerField()
    nombre_usuario = forms.CharField()
    foto_cliente = forms.ImageField()

    class Meta:
        model = Cliente
        fields = ['sexo']