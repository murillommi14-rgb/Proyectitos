# calificaciones/admin.py
# registro en el admin para revisar/editar rápido

from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    # columnas visibles en el listado del admin
    list_display = ("instrumento", "ejercicio", "mercado", "estado", "actualizado_en")
    # filtros laterales
    list_filter = ("ejercicio", "estado", "mercado")
    # buscador
    search_fields = ("instrumento", "mercado")
