from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio),
    path("articulos" , views.articulos, name="articulos"),
    path("clientes" , views.clientes, name="clientes"),
    path("ventas", views.ventas, name="ventas"),
    path("alta_articulos", views.alta_articulos),
    path("alta_clientes", views.alta_clientes),
    path("alta_pedidos", views.alta_pedidos),
    path("buscar_articulos" , views.buscar_articulos),
    path("buscar" , views.buscar)

]

