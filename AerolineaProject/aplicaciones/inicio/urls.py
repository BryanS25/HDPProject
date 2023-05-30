from django.urls import path
from . import views

urlpatterns = [
    path('inicio/index', views.index),
    path('inicio/consultar-precios', views.consultar_precios),
    path('inicio/consultar-precios-js', views.consultar_precios_js),
    path('inicio/consultar-datos-json', views.consultar_datos_json),
    path('inicio/consultar-datos-json2', views.consultar_datos_json2),
    path('inicio/graficar', views.Graficador),
]