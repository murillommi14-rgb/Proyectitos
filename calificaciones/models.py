# modelo principal del MVP
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from .validators import validar_suma_factores_limitada

class Calificacion(models.Model):
    # estados básicos para el flujo
    ESTADOS = [
        ("BORRADOR", "Borrador"),
        ("EN PROCESO", "En Proceso"),
        ("VIGENTE", "Vigente"),
        ("ANULADA", "Anulada"),
        ("INVALIDO", "Inválido"),
    ]

    tipo_mercado = models.CharField(max_length=20, choices=[("ACCIONES", "Acciones"), ("CFI", "CFI"), ("FONDOS_MUTUOS", "Fondos Mutuos"), ("ISIFT", "ISIFT")], help_text="Tipo de Mercado", default="ACCIONES")
    origen = models.CharField(max_length=20, choices=[("CORREDORA", "Corredora"), ("SISTEMA", "Sistema")], help_text="Origen", default="CORREDORA")
    ejercicio = models.DateField(verbose_name="Fecha pago", help_text="Fecha pago", default="2025-01-01")
    mercado = models.CharField(max_length=120, help_text="Mercado", default="")
    instrumento = models.CharField(max_length=120, help_text="Instrumento", default="")
    fecha = models.DateField(help_text="Fecha (DD-MM-AAAA)", default="2025-01-01")
    secuencia = models.IntegerField(verbose_name="Secuencia", help_text="Secuencia", validators=[MinValueValidator(0)], default=0)
    numero_dividendo = models.IntegerField(verbose_name="Número de dividendo", help_text="Número de dividendo", validators=[MinValueValidator(0)], default=0)
    tipo_sociedad = models.CharField(max_length=1, choices=[("A", "Abierta"), ("C", "Cerrada")], help_text="Tipo sociedad A/C", default="A")
    valor_historico = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal("0"), validators=[MinValueValidator(Decimal("0"))])
    isfut_casilla = models.BooleanField(default=False, verbose_name="ISFUT")
    descripcion = models.TextField(max_length=1000, blank=True, default="", verbose_name="Descripción")
    factor_actualizacion = models.DecimalField(max_digits=10, decimal_places=4, default=0.0000, verbose_name="Factor de Actualización")

    # factores 1..26
    factor1 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor2 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor3 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor4 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor5 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor6 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor7 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor8 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor9 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor10 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor11 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor12 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor13 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor14 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor15 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor16 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor17 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor18 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor19 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor20 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor21 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor22 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor23 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor24 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor25 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))
    factor26 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=Decimal("0.0000"))

    estado = models.CharField(max_length=12, choices=ESTADOS, default="BORRADOR")

    # marcas de tiempo
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-actualizado_en"]  # lo más reciente se va para arriba
        indexes = [
            models.Index(fields=["ejercicio"]),
            models.Index(fields=["mercado"]),
            models.Index(fields=["instrumento"]),
            models.Index(fields=["estado"]),
            models.Index(fields=["tipo_mercado"]),
            models.Index(fields=["origen"]),
            models.Index(fields=["ejercicio", "mercado"]),
            models.Index(fields=["instrumento", "estado"]),
        ]

    def clean(self):
        # ejecutamos la regla de negocio ANTES de guardar
        validar_suma_factores_limitada(self)

    def __str__(self):
        return f"{self.instrumento} / {self.ejercicio} / {self.mercado}"
