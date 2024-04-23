# models.py

from django.db import models # type: ignore


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    
# views.py

from django.http import HttpResponse # type: ignore

def lista_libros(request):
    libros = Libro.objects.all()
    salida = ', '.join([l.titulo for l in libros])
    return HttpResponse(salida)