from django.db import models

# Create your models here.

class Catalogacion(models.Model):
	nombre=models.CharField(max_length=60)
	codigo=models.CharField(max_length=60, null=True, blank=True)
	estado=models.BooleanField(default=True)
	class Meta:
		verbose_name="Catalogacion"
		verbose_name_plural="Catalogacions"
	def __str__(self):
		return self.nombre
