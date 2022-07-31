from django import forms

class FormProductos(forms.Form):

    Nombre= forms.CharField()
    Stock= forms.IntegerField()
    Precio= forms.IntegerField()
    Foto= forms.ImageField()

