from django.db import models

# Create your models here.
class Econoclima(models.Model):
    nombre = models.CharField('Nombre', max_length=60)
    agricultura_año = models.IntegerField('Agricultura año', default='0')
    agricultura_perdidas = models.DecimalField('Agricultura perdidas en Millones', max_digits=6, decimal_places=2, default='0')
    salud_año = models.IntegerField('Salud año', null=True)
    salud_perdidas = models.DecimalField('Salud perdidas en Millones', max_digits=6, decimal_places=2, null=True)
    turismo_año = models.IntegerField('Turismo año', null=True)
    turismo_perdidas = models.DecimalField('Turismo perdidas en Millones', max_digits=6, decimal_places=2, null=True)
    infraestructura_año = models.IntegerField('Infraestructura año', null=True)
    infraestructura_perdidas = models.DecimalField('Infraestructura perdidas en Millones', max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.nombre + ' | ' + str(self.agricultura_año) + ' | ' + str(self.agricultura_perdidas)