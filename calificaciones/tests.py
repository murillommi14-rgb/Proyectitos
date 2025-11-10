import pytest
from decimal import Decimal
from django.test import TestCase
from django.core.exceptions import ValidationError
from core.models import User
from django.test import Client
from django.urls import reverse
from .models import Calificacion
from .forms import CalificacionForm, BulkUploadForm
from .validators import validar_suma_factores_limitada
import factory
from datetime import date


class CalificacionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Calificacion

    tipo_mercado = 'ACCIONES'
    origen = 'CORREDORA'
    ejercicio = date.today()
    mercado = 'Test Mercado'
    instrumento = 'Test Instrumento'
    fecha = date.today()
    secuencia = 10000
    numero_dividendo = 0
    tipo_sociedad = 'A'
    valor_historico = Decimal('100.00')
    isfut_casilla = False
    descripcion = 'Test description'
    factor_actualizacion = Decimal('1.0000')
    factor1 = Decimal('0.1000')
    factor2 = Decimal('0.2000')
    estado = 'BORRADOR'


class TestCalificacionModel(TestCase):
    def test_validar_suma_factores_limitada_valid(self):
        calif = CalificacionFactory()
        calif.factor1 = Decimal('0.5000')
        calif.factor2 = Decimal('0.4000')
        validar_suma_factores_limitada(calif)
        self.assertEqual(calif.estado, 'BORRADOR')

    def test_validar_suma_factores_limitada_invalid(self):
        calif = CalificacionFactory()
        calif.factor1 = Decimal('0.6000')
        calif.factor2 = Decimal('0.5000')
        validar_suma_factores_limitada(calif)
        self.assertEqual(calif.estado, 'INVALIDO')

    def test_model_creation(self):
        calif = CalificacionFactory()
        self.assertEqual(calif.tipo_mercado, 'ACCIONES')
        self.assertEqual(calif.origen, 'CORREDORA')

    def test_model_str(self):
        calif = CalificacionFactory()
        expected = f"{calif.instrumento} / {calif.ejercicio} / {calif.mercado}"
        self.assertEqual(str(calif), expected)


class TestCalificacionForm(TestCase):
    def test_form_valid(self):
        data = {
            'tipo_mercado': 'ACCIONES',
            'origen': 'CORREDORA',
            'ejercicio': date.today(),
            'mercado': 'Test Mercado',
            'instrumento': 'Test Instrumento',
            'fecha': date.today(),
            'secuencia': 10000,
            'numero_dividendo': 0,
            'tipo_sociedad': 'A',
            'valor_historico': '100.00',
            'isfut_casilla': False,
            'descripcion': 'Test',
            'factor_actualizacion': '1.0000',
            'factor1': '0.1000',
            'estado': 'BORRADOR',
        }
        form = CalificacionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_missing_required(self):
        data = {}
        form = CalificacionForm(data=data)
        self.assertFalse(form.is_valid())


class TestCalificacionViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_list_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('calificaciones:lista'))
        self.assertEqual(response.status_code, 302)  # Redirigir para iniciar sesión

    def test_list_view_authenticated(self):
        response = self.client.get(reverse('calificaciones:lista'))
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        data = {
            'tipo_mercado': 'ACCIONES',
            'origen': 'CORREDORA',
            'ejercicio': date.today(),
            'mercado': 'Test Mercado',
            'instrumento': 'Test Instrumento',
            'fecha': date.today(),
            'secuencia': 10000,
            'numero_dividendo': 0,
            'tipo_sociedad': 'A',
            'valor_historico': '100.00',
            'isfut_casilla': False,
            'descripcion': 'Test',
            'factor_actualizacion': '1.0000',
            'factor1': '0.1000',
            'estado': 'BORRADOR',
        }
        response = self.client.post(reverse('calificaciones:crear'), data)
        self.assertEqual(response.status_code, 302)  # Redirigir después del éxito
        self.assertEqual(Calificacion.objects.count(), 1)


class TestBulkUpload(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_bulk_upload_form_valid(self):
        form = BulkUploadForm(files={'file': None})  # archivo simulado
        # Agrega aquí las pruebas de validación de archivos.
        pass  # Espacio reservado para pruebas de carga de archivos


# Pruebas de seguridad
class TestSecurity(TestCase):
    def setUp(self):
        self.client = Client()

    def test_csrf_protection(self):
        # Se requiere un token CSRF de prueba para POST
        response = self.client.post(reverse('calificaciones:crear'), {})
        self.assertEqual(response.status_code, 403)  # Prohibido sin CSRF

    def test_sql_injection_prevention(self):
        # Intento de inyección SQL en la búsqueda
        response = self.client.get(reverse('calificaciones:calif_list'), {'mercado': "'; DROP TABLE calificaciones_calificacion; --"})
        # No debería provocar fallos ni eliminar datos.
        self.assertEqual(response.status_code, 200)


# Pruebas de rendimiento (con Locust para pruebas de carga)
# Nota: Ejecutar por separado con `locust -f locustfile.py`

# Para ejecutar las pruebas: pytest
# Cobertura: coverage run --source=. manage.py test && coverage report
