# formulario basado en modelo (para crear/editar rápido)
from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = [
            "tipo_mercado","origen","mercado","instrumento","secuencia","numero_dividendo","tipo_sociedad","fecha","valor_historico","ejercicio","descripcion","isfut_casilla","factor_actualizacion",
            "factor1","factor2","factor3","factor4","factor5","factor6","factor7","factor8","factor9","factor10","factor11","factor12","factor13","factor14","factor15","factor16","factor17","factor18","factor19","factor20","factor21","factor22","factor23","factor24","factor25","factor26",
            "estado",
        ]
        widgets = {
            "mercado": forms.TextInput(attrs={'autocomplete': 'off'}),
            "instrumento": forms.TextInput(attrs={'autocomplete': 'off'}),
            "secuencia": forms.NumberInput(attrs={'min': '10000'}),
            "numero_dividendo": forms.NumberInput(attrs={'value': '0', 'min': '0'}),
            "fecha": forms.DateInput(attrs={'type': 'date'}),
            "valor_historico": forms.NumberInput(attrs={'min': '0'}),
            "ejercicio": forms.DateInput(attrs={'type': 'date'}),
            "descripcion": forms.Textarea(attrs={'rows': 3, 'maxlength': 1000, 'style': 'resize: none;'}),
            "isfut_casilla": forms.CheckboxInput(),
            "factor_actualizacion": forms.NumberInput(attrs={'value': '0', 'step': '0.0001', 'min': '0'}),
            "estado": forms.Select(),
            "factor1": forms.NumberInput(attrs={'min': '0'}),
            "factor2": forms.NumberInput(attrs={'min': '0'}),
            "factor3": forms.NumberInput(attrs={'min': '0'}),
            "factor4": forms.NumberInput(attrs={'min': '0'}),
            "factor5": forms.NumberInput(attrs={'min': '0'}),
            "factor6": forms.NumberInput(attrs={'min': '0'}),
            "factor7": forms.NumberInput(attrs={'min': '0'}),
            "factor8": forms.NumberInput(attrs={'min': '0'}),
            "factor9": forms.NumberInput(attrs={'min': '0'}),
            "factor10": forms.NumberInput(attrs={'min': '0'}),
            "factor11": forms.NumberInput(attrs={'min': '0'}),
            "factor12": forms.NumberInput(attrs={'min': '0'}),
            "factor13": forms.NumberInput(attrs={'min': '0'}),
            "factor14": forms.NumberInput(attrs={'min': '0'}),
            "factor15": forms.NumberInput(attrs={'min': '0'}),
            "factor16": forms.NumberInput(attrs={'min': '0'}),
            "factor17": forms.NumberInput(attrs={'min': '0'}),
            "factor18": forms.NumberInput(attrs={'min': '0'}),
            "factor19": forms.NumberInput(attrs={'min': '0'}),
            "factor20": forms.NumberInput(attrs={'min': '0'}),
            "factor21": forms.NumberInput(attrs={'min': '0'}),
            "factor22": forms.NumberInput(attrs={'min': '0'}),
            "factor23": forms.NumberInput(attrs={'min': '0'}),
            "factor24": forms.NumberInput(attrs={'min': '0'}),
            "factor25": forms.NumberInput(attrs={'min': '0'}),
            "factor26": forms.NumberInput(attrs={'min': '0'}),
        }
        labels = {
            "factor1": "Factor 1: Divide la columna: Con crédito por IDPC generados a contar del 01.01.2017 / Suma de la columna 8 a la 19",
            "factor2": "Factor 2: Divide la columna:Con crédito por IDPC acumulados hasta el 31.12.2016 / Suma de la columna 8 a la 19",
            "factor3": "Factor 3: Divide la columna:Con  derecho a crédito por pago de IDPC voluntario/ Suma de la columna 8 a la 19",
            "factor4": "Factor 4: Divide la columna:Sin derecho a crédito/ Suma de la columna 8 a la 19",
            "factor5": "Factor 5: Divide la columna:Rentas provenientes del registro RAP y Diferencia Inicial de sociedad acogida al ex Art. 14 TER A) LIR/ Suma de la columna 8 a la 19",
            "factor6": "Factor 6: Divide la columna:Otras rentas percibidas Sin Prioridad en su orden de imputación/ Suma de la columna 8 a la 19",
            "factor7": "Factor 7: Divide la columna:Exceso Distribuciones Desproporcionadas (N°9 Art.14 A)/ Suma de la columna 8 a la 19",
            "factor8": "Factor 8: Divide la columna:Utilidades afectadas con impuesto sustitutivo al FUT (ISFUT) Ley N°20.780 / Suma de la columna 8 a la 19",
            "factor9": "Factor 9: Divide la columna:Rentas generadas hasta el 31.12.1983 y/o utilidades afectadas con impuesto sustitutivo al FUT (ISFUT) LEY N°21.210 / Suma de la columna 8 a la 19",
            "factor10": "Factor 10: Divide la columna:Rentas Exentas de Impuesto Global Complementario (IGC) (Artículo 11, Ley 18.401), Afectas a Impuesto Adicional / Suma de la columna 8 a la 19",
            "factor11": "Factor 11: Divide la columna:Rentas Exentas de Impuesto Global Complementario (IGC) y/o Impuesto Adicional (IA)/ Suma de la columna 8 a la 19",
            "factor12": "Factor 12: Divide la columna:Ingresos No Constitutivos de  Renta/ Suma de la columna 8 a la 19",
            "factor13": "Factor 13: Divide la columna:No Sujetos a Restitución generados Hasta el 31.12.2019 Sin derecho / Suma de la columna 8 a la 1",
            "factor14": "Factor 14: Divide la columna:No Sujetos a Restitución generados Hasta el 31.12.2019 Con derecho / Suma de la columna 8 a la 19",
            "factor15": "Factor 15: Divide la columna:No Sujetos a Restitución generados a contar del 01.01.2020 Sin derecho / Suma de la columna 8 a la 19",
            "factor16": "Factor 16: Divide la columna:No Sujetos a Restitución generados a contar del 01.01.2020 Con derecho / Suma de la columna 8 a la 19",
            "factor17": "Factor 17: Divide la columna:Sujeto a restitución sin derecho / Suma de la columna 8 a la 19",
            "factor18": "Factor 18: Divide la columna:Sujeto a restitución Con derecho / Suma de la columna 8 a la 19",
            "factor19": "Factor 19: Divide la columna:Sujeto a restitución Sin derecho / Suma de la columna 8 a la 19",
            "factor20": "Factor 20: Divide la columna:Sujeto a restitución Con derecho / Suma de la columna 8 a la 19",
            "factor21": "Factor 21: Divide la columna:Credito IPE/ Suma de la columna 8 a la 19",
            "factor22": "Factor 22: Divide la columna:Asociados a Rentas Afectas, sin derecho/ Suma de la columna 8 a la 19",
            "factor23": "Factor 23: Divide la columna:Asociados a Rentas Afectas, Con derecho/ Suma de la columna 8 a la 19",
            "factor24": "Factor 24: Divide la columna:Asociados a Rentas Exentas (artículo 11, Ley 18.401), sin derecho/ Suma de la columna 8 a la 19",
            "factor25": "Factor 25: Divide la columna:Asociados a Rentas Exentas (artículo 11, Ley 18.401), con  derecho/ Suma de la columna 8 a la 19",
            "factor26": "Factor 26: Divide la columna:Crédito por IPE / Suma de la columna 8 a la 19",
        }

class BulkUploadForm(forms.Form):
    file = forms.FileField(label="Archivos CSV o XLSX", help_text="Sube uno o más archivos con las calificaciones", widget=forms.ClearableFileInput(attrs={'multiple': True}))
