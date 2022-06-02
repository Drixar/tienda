from django.http import HttpResponse
from django.shortcuts import render
from stock.models import Articulos, Ventas, Cliente, Pedido
from django.template import loader

# Create your views here.

def inicio(reqest):
    return HttpResponse()

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