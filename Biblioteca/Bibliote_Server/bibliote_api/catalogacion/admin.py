from django.contrib import admin
from .models.Categoria import Categoria
from .models.Autor import Autor
#from .models.Libro import Libro
#from .models.Ejemplar import Ejemplar
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
	"""docstring for CategoriaAdmin"""
	list_display=("nombre","codigo","estado")
	search_fields=("nombre","codigo",)
	list_per_page=3

admin.site.register(Categoria, CategoriaAdmin)
