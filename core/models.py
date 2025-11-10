from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    ROLE_CHOICES = [
        ('LIDER_PRODUCTO', 'Líder de producto'),
        ('ANALISTA_PROCESOS', 'Analista de procesos'),
        ('INGENIERO_DATOS', 'Ingeniero de datos'),
        ('REPRESENTANTE_TRIBUTARIO', 'Representante tributario'),
        ('ENCARGADO_SEGURIDAD_TI', 'Encargado de seguridad TI'),
    ]

    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class User(AbstractUser):
    roles = models.ManyToManyField(Role, blank=True)

    def __str__(self):
        return self.username
