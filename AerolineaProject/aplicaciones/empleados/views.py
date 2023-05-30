from django.shortcuts import render
from .models import Empleado
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from .models import Administrador

#Create you views hehre.
def lista_empleados(request):
    datos = {
        'lista': Empleado.objects.all().order_by('id'),
        'titulo': 'Lista de empleados',
    }
    return render(request, 'empleados/lista-empleados-2.html', datos)

class CrearEmpleado(CreateView):
    template_name = 'empleados/crear-empleado.html'
    model = Empleado
    fields = ['nombre', 'correo', 'sueldo']
    success_url = reverse_lazy('empleados_app:lista-empleados')

from django.contrib.messages.views import SuccessMessageMixin
class ModificarEmpleado(SuccessMessageMixin, UpdateView):
    template_name = 'empleados/modificar-empleado.html'
    model = Empleado
    fields = ['nombre', 'correo', 'sueldo']
    success_url = reverse_lazy('empleados_app:lista-empleados')
    success_message = "El registro %(nombre)s fue modificado exitosamente"
    
class EliminarEmpleado(SuccessMessageMixin, DeleteView):
    template_name = 'empleados/eliminar-empleado.html'
    model = Empleado
    success_url = reverse_lazy('empleados_app:lista-empleados')
    success_message = "El registro fue eliminado exitosamente"
