# ver la bitacora en /admin 
from django.contrib import admin
from .models import Auditoria

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ("timestamp","accion","modelo","objeto_id","usuario","ip")
    list_filter = ("accion","modelo","usuario")
    search_fields = ("modelo","objeto_id","detalle","user_agent")
