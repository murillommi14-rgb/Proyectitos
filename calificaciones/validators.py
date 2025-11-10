# reglas de negocio aquí va la famosa suma de factores <= 1
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from decimal import Decimal
import re

def validar_suma_factores_limitada(instance):
    # sumamos factor1..factor26, si pasa de 1, marcamos como INVALIDO
    total = sum([
        instance.factor1 or Decimal("0"),
        instance.factor2 or Decimal("0"),
        instance.factor3 or Decimal("0"),
        instance.factor4 or Decimal("0"),
        instance.factor5 or Decimal("0"),
        instance.factor6 or Decimal("0"),
        instance.factor7 or Decimal("0"),
        instance.factor8 or Decimal("0"),
        instance.factor9 or Decimal("0"),
        instance.factor10 or Decimal("0"),
        instance.factor11 or Decimal("0"),
        instance.factor12 or Decimal("0"),
        instance.factor13 or Decimal("0"),
        instance.factor14 or Decimal("0"),
        instance.factor15 or Decimal("0"),
        instance.factor16 or Decimal("0"),
        instance.factor17 or Decimal("0"),
        instance.factor18 or Decimal("0"),
        instance.factor19 or Decimal("0"),
        instance.factor20 or Decimal("0"),
        instance.factor21 or Decimal("0"),
        instance.factor22 or Decimal("0"),
        instance.factor23 or Decimal("0"),
        instance.factor24 or Decimal("0"),
        instance.factor25 or Decimal("0"),
        instance.factor26 or Decimal("0"),
    ])
    if total > Decimal("1"):
        instance.estado = 'INVALIDO'

# Validadores para campos
corredor_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9\s\-]*$',
    message="El corredor solo puede contener letras, números, espacios y guiones.",
    code='invalid_corredor'
)

instrumento_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9\s\-\/]*$',
    message="El instrumento solo puede contener letras, números, espacios, guiones y barras.",
    code='invalid_instrumento'
)

def validar_anio(value):
    if not (1900 <= value <= 2025):
        raise ValidationError("El año debe estar entre 1900 y 2025.")

def validar_monto(value):
    if value < 0:
        raise ValidationError("El monto no puede ser negativo.")
