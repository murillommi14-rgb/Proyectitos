# bitacora
from django.db import models
from django.conf import settings

class Auditoria(models.Model):
    accion = models.CharField(max_length=30)        # CREADO / ACTUALIZADO / ELIMINADO
    modelo = models.CharField(max_length=120)       # nombre del modelo afectado
    objeto_id = models.CharField(max_length=120)    # id del objeto
    detalle = models.TextField(blank=True, default="")  # informacion util (estado, monto, etc)

    # quien lo hizo (puede ser null si no hay usuario)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="auditorias"
    )

    # metadatos de la solicitud
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, default="")

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"[{self.timestamp:%Y-%m-%d %H:%M}] {self.accion} {self.modelo}#{self.objeto_id}"
