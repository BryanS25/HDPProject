from django.shortcuts import render
from .models import Econoclima
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import matplotlib.pyplot as plt
import io
import urllib, base64
#import plotly.graph_objects as go
#from .models import Administrador

#Create you views hehre.
def lista_empleados(request):
    datos = {
        'lista': Econoclima.objects.all().order_by('id'),
        'titulo': 'Lista de empleados',
    }
    return render(request, 'empleados/lista-empleados-2.html', datos)

def getSetNombre():
    elements = Econoclima.objects.all().order_by('id')
    choices = []
    for element in elements:
        choices.append((element.nombre))
    return choices    

def getSetSueldo():
    elements = Econoclima.objects.all()
    choices = []
    for element in elements:
        choices.append((element.sueldo))
    return choices

def getSetAgriculturaAño():
    elements = Econoclima.objects.all()
    choices = []
    for element in elements:
        choices.append((element.agricultura_año))
    return choices

def getSetAgriculturaPerdidas():
    elements = Econoclima.objects.all()
    choices = []
    for element in elements:
        choices.append((element.agricultura_perdidas))
    return choices

def getSetSaludAño():
    elements = Econoclima.objects.all()
    choices = []
    for element in elements:
        choices.append((element.salud_año))
    return choices

def getSetSaludPerdidas():
    elements = Econoclima.objects.all()
    choices = []
    for element in elements:
        choices.append((element.salud_perdidas))
    return choices

def getSetTurismoAño():
    elements = Econoclima.objects.all()
    choices = []
    for element in elements:
        choices.append((element.turismo_año))
    return choices

def getSetTurismoPerdidas():
    elements = Econoclima.objects.all()
    choices = []
    for element in elements:
        choices.append((element.turismo_perdidas))
    return choices

def getSetInfraestructuraAño():
    elements = Econoclima.objects.all()
    choices = []
    for element in elements:
        choices.append((element.infraestructura_año))
    return choices

def getSetInfraestructuraPerdidas():
    elements = Econoclima.objects.all()
    choices = []
    for element in elements:
        choices.append((element.infraestructura_perdidas))
    return choices
##################################################################
def Graficador(request):
    #x = getSetNombre()
    #y = getSetSueldo()
    a = getSetNombre()
    b = getSetAgriculturaPerdidas()

    #plt.bar(x, y)
    #plt.xlabel('Eje X')
    #plt.ylabel('Eje Y')
    #plt.title('Gráfico de barras')
    plt.figure(figsize=(6.3,4))
    plt.bar(a, b, color='green')
    plt.xlabel('Años')
    plt.ylabel('Perdidas en millones')
    plt.title('Agricultura')
    
    # Convertir el gráfico en una imagen
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    x = getSetNombre()
    y = getSetInfraestructuraPerdidas()

    plt.figure(figsize=(6.3,4))
    #plt.subplot(1, 2, 2)
    plt.bar(x, y, color='blue')
    plt.xlabel('Años')
    plt.ylabel('Perdidas en millones')
    plt.title('Infraestructura')

    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_png2 = buffer2.getvalue()
    buffer.close()

    graphic2 = base64.b64encode(image_png2)
    graphic2 = graphic2.decode('utf-8')


    c = getSetNombre()
    d = getSetSaludPerdidas()

    plt.figure(figsize=(6.3,4))
    plt.bar(c, d, color='red')
    plt.xlabel('Años')
    plt.ylabel('Perdidas en millones')
    plt.title('Salud')

    buffer3 = io.BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    image_png3 = buffer3.getvalue()
    buffer3.close()

    graphic3 = base64.b64encode(image_png3)
    graphic3 = graphic3.decode('utf-8')

    e = getSetNombre()
    f = getSetTurismoPerdidas()

    plt.figure(figsize=(6.3,4))
    #plt.subplot(2, 2, 4)
    plt.bar(e, f, color='orange')
    plt.xlabel('Años')
    plt.ylabel('Perdidas en millones')
    plt.title('Turismo')

    buffer4 = io.BytesIO()
    plt.savefig(buffer4, format='png')
    buffer4.seek(0)
    image_png4 = buffer4.getvalue()
    buffer4.close()

    graphic4 = base64.b64encode(image_png4)
    graphic4 = graphic4.decode('utf-8')

    #plt.tight_layout()

    return render(request, 'empleados/graficar1.html', {'graphic': graphic, 'graphic2': graphic2, 'graphic3': graphic3, 'graphic4': graphic4})


###########################################################################
###########################################################################

def agricultura(request):
    template_name = 'empleados/agricultura.html'
    success_url = reverse_lazy('econoclima_app:agricultura')
    return render(request, 'empleados/agricultura.html')

def infraestructura(request):
    template_name = 'empleados/infraestructura.html'
    success_url = reverse_lazy('econoclima_app:infraestructura')
    return render(request, 'empleados/infraestructura.html')

def salud(request):
    template_name = 'empleados/salud.html'
    success_url = reverse_lazy('econoclima_app:salud')
    return render(request, 'empleados/salud.html')

def turismo(request):
    template_name = 'empleados/turismo.html'
    success_url = reverse_lazy('econoclima_app:turismo')
    return render(request, 'empleados/turismo.html')

def admin2(request):
    template_name = 'empleados/admin2.html'
    success_url = reverse_lazy('econoclima_app:admin2')
    return render(request, 'empleados/admin2.html')

def recursos(request):
    template_name = 'empleados/recursos.html'
    success_url = reverse_lazy('econoclima_app:recursos')
    return render(request, 'empleados/recursos.html')

def recomendaciones(request):
    template_name = 'empleados/recomendaciones.html'
    success_url = reverse_lazy('econoclima_app:recomendaciones')
    return render(request, 'empleados/recomendaciones.html')

###########################################################################

class Creardato(CreateView):
    template_name = 'empleados/crear-dato.html'
    model = Econoclima
    fields = ['nombre', 'agricultura_año', 'agricultura_perdidas', 'salud_año', 'salud_perdidas', 'turismo_año', 'turismo_perdidas', 'infraestructura_año', 'infraestructura_perdidas']
    success_url = reverse_lazy('econoclima:lista-empleados')

from django.contrib.messages.views import SuccessMessageMixin
class Modificardato(SuccessMessageMixin, UpdateView):
    template_name = 'empleados/modificar-dato.html'
    model = Econoclima
    fields = ['nombre', 'agricultura_año', 'agricultura_perdidas', 'salud_año', 'salud_perdidas', 'turismo_año', 'turismo_perdidas', 'infraestructura_año', 'infraestructura_perdidas']
    success_url = reverse_lazy('econoclima_app:lista-empleados')
    success_message = "El registro de año %(agricultura_año)s fue modificado exitosamente"
    
class Eliminardato(SuccessMessageMixin, DeleteView):
    template_name = 'empleados/eliminar-dato.html'
    model = Econoclima
    success_url = reverse_lazy('econoclima_app:lista-empleados')
    success_message = "El registro fue eliminado exitosamente"
