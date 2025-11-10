import pytest
from django.test import TestCase
from core.models import User
from django.db.models.signals import post_save, post_delete
from .models import Auditoria
from calificaciones.models import Calificacion
from datetime import date
from decimal import Decimal
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')


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


class TestAuditoriaModel(TestCase):
    def test_auditoria_creation(self):
        user = UserFactory()
        audit = Auditoria.objects.create(
            accion='CREADO',
            modelo='Calificacion',
            objeto_id='1',
            detalle='Test detalle',
            usuario=user,
            ip='127.0.0.1',
            user_agent='Test Agent'
        )
        self.assertEqual(audit.accion, 'CREADO')
        self.assertEqual(audit.modelo, 'Calificacion')
        self.assertEqual(audit.usuario, user)

    def test_auditoria_str(self):
        audit = Auditoria.objects.create(
            accion='ACTUALIZADO',
            modelo='Calificacion',
            objeto_id='1',
            detalle='Test'
        )
        expected = f"Auditoria: ACTUALIZADO - Calificacion - 1"
        self.assertEqual(str(audit), expected)


class TestAuditoriaSignals(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_post_save_signal_create(self):
        # Desconecta y vuelve a conectar para evitar interferencias
        from .signals import audit_post_save
        post_save.disconnect(sender=Calificacion)
        post_save.connect(audit_post_save, sender=Calificacion)

        calif = CalificacionFactory()
        calif.save()

        audits = Auditoria.objects.filter(modelo='Calificacion', objeto_id=str(calif.pk))
        self.assertEqual(audits.count(), 1)
        self.assertEqual(audits.first().accion, 'CREADO')

    def test_post_save_signal_update(self):
        calif = CalificacionFactory()
        calif.save()

        calif.estado = 'VIGENTE'
        calif.save()

        audits = Auditoria.objects.filter(modelo='Calificacion', objeto_id=str(calif.pk))
        self.assertEqual(audits.count(), 2)
        self.assertIn('ACTUALIZADO', [a.accion for a in audits])

    def test_post_delete_signal(self):
        calif = CalificacionFactory()
        calif.save()
        pk = calif.pk

        calif.delete()

        audits = Auditoria.objects.filter(modelo='Calificacion', objeto_id=str(pk))
        self.assertEqual(audits.count(), 2)  # Crear + Eliminar
        self.assertIn('ELIMINADO', [a.accion for a in audits])


# Para ejecutar las pruebas: pytest auditoria/tests.py