from django.shortcuts import render
import requests
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64

# Create your views here.
def index(request):
    return render(request, 'inicio/index.html')

def consultar_precios(request):
    pagina = 1
    if request.GET:
        pagina=int(request.GET['page'])

    url_binance = 'https://api.binance.com/api/v3/ticker/price'
    datos = requests.get(url_binance)

    contexto = {'precios':datos.json()[pagina*10-10:pagina*10:]}
    return render(request, 'inicio/consultar-precios.html', contexto)

############################################################
def Graficador(request):
    x = [1, 2, 3, 4, 5]
    y = [10, 5, 7, 3, 8]
    
    plt.bar(x, y)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfico de barras')
    
    # Convertir el gráfico en una imagen
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'inicio/graficar.html', {'graphic': graphic})
####################################################################
def consultar_precios_js(request):
    return render(request, 'inicio/consultar-precios-js.html')


def consultar_datos_json(request):

    url_json = 'https://jsonplaceholder.typicode.com/users'
    info = requests.get(url_json)

    contexto2 = {'info':info.json()}
    return render(request, 'inicio/consultar-datos-json.html', contexto2)

def consultar_datos_json2(request):
    url_json2 = 'https://jsonplaceholder.typicode.com/posts/1'
    usauario = requests.get(url_json2)

    contexto3 = {'usuario':usauario.json()}
    return render(request, 'inicio/consultar-datos-json2.html', contexto3)