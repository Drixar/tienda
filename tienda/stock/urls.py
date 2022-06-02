from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio),
    path("articulos" , views.articulos),
    path("clientes" , views.clientes),
    path("ventas", views.ventas)

]