from django.db import models

from apps.adopcion.models import Persona


class Vacuna(models.Model):
	nombre = models.CharField(max_length=50)
	#Una mascota puede tener aplicadas varias vacunas
	####### MUCHOS A MUCHOS #######

	def __str__(self):
		return '{}'.format(self.nombre)

class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	####### UNO A MUCHOS #######
	#Atributo extendido de la tabla Persona
	#Persona: modelo externo
	#null=True: Permite campos con valor nulo
	#blank: permite guardar sin haber ingresado ningun dato
	#on_delete: para borrar automaticamente de persona como de mascota
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna, blank=True)


	#una persona solo puede aceptar una mascota
	####### UNO A UNO #######
	#persona = models.OneToOneField(Persona, null=True, blank=True, on_delete=models.CASCADE)

