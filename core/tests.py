import pytest
from django.test import TestCase, RequestFactory
from .models import User, Role
from django.http import HttpRequest
from .middleware import CurrentRequestMiddleware, get_current_request, get_current_user, get_ip_and_ua
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')


class RoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role

    name = factory.Sequence(lambda n: f'Role {n}')


class TestRoleModel(TestCase):
    def test_role_creation(self):
        role = RoleFactory()
        self.assertEqual(role.name, 'Role 0')

    def test_role_str(self):
        role = RoleFactory(name='Admin')
        self.assertEqual(str(role), 'Admin')


class TestUserModel(TestCase):
    def test_user_creation(self):
        user = UserFactory()
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.email, 'user1@example.com')

    def test_user_roles(self):
        user = UserFactory()
        role1 = RoleFactory()
        role2 = RoleFactory()
        user.roles.add(role1, role2)
        self.assertEqual(user.roles.count(), 2)


class TestCurrentRequestMiddleware(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = CurrentRequestMiddleware(lambda r: None)

    def test_middleware_stores_request(self):
        request = self.factory.get('/')
        request.user = UserFactory()
        self.middleware(request)
        self.assertEqual(get_current_request(), request)
        self.assertEqual(get_current_user(), request.user)

    def test_get_ip_and_ua(self):
        request = self.factory.get('/', HTTP_X_FORWARDED_FOR='192.168.1.1, 10.0.0.1', HTTP_USER_AGENT='Test UA')
        ip, ua = get_ip_and_ua()
        # Dado que no se ha llamado al middleware, debería devolver None, ""
        self.assertIsNone(ip)
        self.assertEqual(ua, "")

        # Con middleware
        self.middleware(request)
        ip, ua = get_ip_and_ua()
        self.assertEqual(ip, '192.168.1.1')
        self.assertEqual(ua, 'Test UA')


# Para ejecutar las pruebas: pytest core/tests.py
