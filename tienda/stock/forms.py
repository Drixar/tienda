from django import forms


class Alta_articulos(forms.Form):

    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length= 30)
    descripcion = forms.CharField(max_length= 40)
    seccion = forms.CharField(max_length= 20)
    precio = forms.IntegerField()
    stock = forms.IntegerField()

class Alta_clientes(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField(max_length= 40)
    direccion = forms.CharField(max_length= 40)
    telefono = forms.CharField(max_length= 15)

class Alta_pedidos(forms.Form):
    numero = forms.IntegerField()
    fecha = forms.DateField()
    cliente = forms.IntegerField()
    entregado = forms.BooleanField()