from django.db import models

FISICO='FISICO'
VIRTUAL='VIRTUAL'
FIS_VIR='FIS_VIR'

LIBRO_TIPO_CHOICES=(
	('','Seleccionar'),
	(FISICO,'Fisico'),
	(VIRTUAL,'Virtual'),
	(FIS_VIR,'FisicoVirtual'),
)