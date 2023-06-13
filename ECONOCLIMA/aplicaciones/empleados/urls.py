from django.urls import path
from . import views
app_name = 'econoclima_app'
urlpatterns = [
    path('empleado/lista-empleados/', views.lista_empleados, name = 'lista-empleados'),
    path('empleado/crear-empleado/', views.Creardato.as_view(), name = 'crear-empleado'),
    path('empleado/modificar-empleado/<pk>/', views.Modificardato.as_view(), name = 'modificar-empleado'),
    path('empleado/eliminar-empleado/<pk>/', views.Eliminardato.as_view(), name = 'eliminar-empleado'),
    path('empleado/graficar1', views.Graficador, name='graficador'),
    #path('empleado/graficar1', views.Graficador2, name='graficador2'),
    path('empleado/agricultura/', views.agricultura, name = 'agricultura'),
    path('empleado/infraestructura/', views.infraestructura, name = 'infraestructura'),
    path('empleado/salud/', views.salud, name = 'salud'),
    path('empleado/turismo/', views.turismo, name = 'turismo'),
    path('empleado/admin2/', views.admin2, name = 'admin2'),
    path('empleado/recursos/', views.recursos, name = 'recursos'),
    path('empleado/recomendaciones/', views.recomendaciones, name = 'recomendaciones'),
    #path('empleado/graficar1', views.Graficador2),
]