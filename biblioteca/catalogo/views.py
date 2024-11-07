# biblioteca/catalogo/views.py
from django.shortcuts import render

def libros(request):
    return render(request, 'catalogo/libros.html')
