from django.http import HttpResponse
from django.shortcuts import render
from stock.models import Articulos, Ventas, Cliente, Pedido
from django.template import loader
from stock.forms import Alta_articulos, Alta_clientes, Alta_pedidos

# Create your views here.

def inicio(request):
    return render( request , "plantilla.html" )

def articulos(request):
    articulos = Articulos.objects.all()
    dicc = {"articulos" : articulos}
    plantilla = loader.get_template("articulos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def clientes(request):
    clientes = Cliente.objects.all()
    dicc = {"clientes" : clientes}
    plantilla = loader.get_template("clientes.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def ventas(request):
    ventas = Ventas.objects.all()
    dicc = {"ventas" : ventas}
    plantilla = loader.get_template("ventas.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def alta_articulos(request):
    if request.method == "POST":
        mi_formulario = Alta_articulos( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data    
            articulos = Articulos( codigo=datos['codigo'] , nombre=datos['nombre'], descripcion=datos['descripcion'], seccion=datos['seccion'], precio=datos['precio'], stock=datos['stock'])
            articulos.save()
            return HttpResponse("Se Creó el Articulo")

    return render( request, "alta_articulos.html")

def alta_clientes(request):
    if request.method == "POST":
        mi_formulario = Alta_clientes( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data    
            clientes = Cliente( dni=datos['dni'] , nombre=datos['nombre'], direccion=datos['direccion'], telefono=datos['telefono'])
            clientes.save()
            return HttpResponse("Se Creó el Cliente")

    return render( request, "alta_clientes.html")

def alta_pedidos(request):
    if request.method == "POST":
        mi_formulario = Alta_pedidos( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data    
            clientes = Pedido( numero=datos['numero'] , fecha=datos['fecha'], cliente=datos['cliente'], entregado=datos['entregado'])
            clientes.save()
            return render( request , "alta_pedidos.html")

    return render( request, "alta_pedidos.html")
    


def buscar_articulos(request):

    return render( request , "buscar_articulo.html")


def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        articulos = Articulos.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado.html" , {"articulos": articulos})
    else:
        return HttpResponse("Campo vacio")
   