from tkinter import ALL
from django import forms
from WebApp.models import Empleado, Cliente, Productos

class FormProductos(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ('__all__')

class FormEmpleado(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ('__all__')
    

class FormCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('__all__')