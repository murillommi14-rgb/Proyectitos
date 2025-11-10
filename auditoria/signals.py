# señales que escriben en la bitácora cuando cambia Calificacion
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from calificaciones.models import Calificacion
from .models import Auditoria
from core.middleware import get_current_user, get_ip_and_ua  # para saber quien/ip/ua

@receiver(post_save, sender=Calificacion)
def auditar_guardado(sender, instance, created, **kwargs):
    accion = "CREADO" if created else "ACTUALIZADO"
    usuario = get_current_user()
    ip, ua = get_ip_and_ua()
    Auditoria.objects.create(
        accion=accion,
        modelo=sender.__name__,
        objeto_id=str(instance.pk),
        detalle=f"Estado={instance.estado}; Valor Historico={instance.valor_historico}",
        usuario=usuario,
        ip=ip,
        user_agent=ua,
    )

@receiver(post_delete, sender=Calificacion)
def auditar_borrado(sender, instance, **kwargs):
    usuario = get_current_user()
    ip, ua = get_ip_and_ua()
    Auditoria.objects.create(
        accion="ELIMINADO",
        modelo=sender.__name__,
        objeto_id=str(instance.pk),
        detalle=f"Instrumento={instance.instrumento}; Ejercicio={instance.ejercicio}",
        usuario=usuario,
        ip=ip,
        user_agent=ua,
    )
