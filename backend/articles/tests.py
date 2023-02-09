from django.test import TestCase
from rest_framework.test import APITestCase

def funcion_suma_str(a, b):
    return str(a + b)

def funcion_multiplicacion(a, b):
    if a < 0:
        raise ValueError("A no puede ser menor que 0")
    return a * b


class ArticleTestCase(TestCase):
    """
    Tests using django TestCase
    """

    def setUp(self):
        # poner codigo que se repite al inicio de todos los tests
        pass

    def tearDown(self):
        # poner codigo que se repite al final de todos los tests
        pass

    def numero_test(self, numero):
        # se pueden crear funciones auxiliares
        pass

    # def test_funcion_suma_str(self):
    #     resultado = funcion_suma_str(2, 3)
    #     self.assertEqual(resultado, '5')

    # def test_funcion_multiplicacion(self):
    #     resultado = funcion_multiplicacion(2, 3)
    #     self.assertEqual(resultado, 6)
    #     self.assertTrue(resultado > 0)
    #     self.assertFalse(resultado > 100)

    # def test_funcion_multiplicacion_salta_error_con_a_menor_0(self):
    #     with self.assertRaises(ValueError):
    #         # ejecutar funcion que da error
    #         resultado = funcion_multiplicacion(-1, 10)

from django.contrib.auth.models import User
from articles.models import Comment
from django.urls import reverse
from articles.factories import CommentFactory, UserFactory
import random

class CommentTestCase(APITestCase):
    """
    Tests using django APITestCase de DRF
    """

    def setUp(self):
        # poner codigo que se repite al inicio de todos los tests
        pass

    def tearDown(self):
        # poner codigo que se repite al final de todos los tests
        pass

    def numero_test(self, numero):
        # se pueden crear funciones auxiliares
        pass

    def test_comments_list_return_all_instances(self):
        user_test = User.objects.create(username="test", email="test@gmail.com")

        Comment.objects.create(user=user_test, body="lorem ipsum")
        Comment.objects.create(user=user_test, body="dolor sit")
        Comment.objects.create(user=user_test, body="dolor sit")

        response = self.client.get(reverse('hola-list'))

        self.assertEqual(len(response.data), 3)

    def test_comments_list_return_filtered_instances_by_user(self):
        """
        Test list endpoint returns instances filtered by user id
        """
        user_test_in = User.objects.create(username="test", email="test@gmail.com")
        user_test_out = User.objects.create(username="out", email="test2@gmail.com")

        Comment.objects.create(user=user_test_in, body="lorem ipsum")
        Comment.objects.create(user=user_test_in, body="dolor sit")
        Comment.objects.create(user=user_test_in, body="dolor sit")

        Comment.objects.create(user=user_test_out, body="lorem ipsum")
        Comment.objects.create(user=user_test_out, body="dolor sit")
        response = self.client.get(reverse('hola-list'), {"user": user_test_in.id})

        self.assertEqual(len(response.data), 3)

        response = self.client.get(reverse('hola-list'), {"user": user_test_in.id})

        self.assertEqual(len(response.data), 3)

    def test_comments_retrieve_instance(self):
        """
        Test retrieve endpoint returns an instance
        """
        user = User.objects.create(username="test", email="test@gmail.com")
        comment = Comment.objects.create(user=user, body="lorem ipsum")

        response = self.client.get(reverse('hola-detail', args=[comment.id]))

        self.assertEqual(response.data["user"], user.id)
        self.assertTrue(response.data.get("body"))

    def test_comments_creates_instances(self):
        """
        Test create endpoint register an instance
        """
        user = User.objects.create(username="test", email="test@gmail.com")

        data = {
            "user": user.id,
            "body": "prueba"
        }

        response = self.client.post(reverse('hola-list'), data)

        self.assertEqual(response.status_code, 201)

        registered_comments = Comment.objects.filter(user=user).count()
        self.assertEqual(registered_comments, 1)



class CommentTestCaseWithFactories(APITestCase):
    """
    Tests using django APITestCase de DRF
    """

    def setUp(self):
        # poner codigo que se repite al inicio de todos los tests
        pass

    def tearDown(self):
        # poner codigo que se repite al final de todos los tests
        pass

    def numero_test(self, numero):
        # se pueden crear funciones auxiliares
        pass

    def test_comments_list_return_all_instances_with_factories(self):
        user = UserFactory()
        _ = [CommentFactory(user=user) for n in range(3)]

        response = self.client.get(reverse('hola-list'))

        self.assertEqual(len(response.data), 3)

    def test_comments_list_return_filtered_instances_by_user_with_factory(self):
        """
        Test list endpoint returns instances filtered by user id
        """
        user_test_in = UserFactory()
        instances_to_create = random.randint(3, 10)

        _ = [CommentFactory(user=user_test_in) for n in range(instances_to_create)]
        _ = [CommentFactory() for n in range(random.randint(1, 4))]

        response = self.client.get(reverse('hola-list'), {"user": user_test_in.id})

        self.assertEqual(len(response.data), instances_to_create)

    def test_comments_retrieve_instance_with_factory(self):
        """
        Test retrieve endpoint returns an instance
        """
        comment = CommentFactory()
        response = self.client.get(reverse('hola-detail', args=[comment.id]))

        self.assertEqual(response.data["user"], comment.user.id)
        self.assertTrue(response.data.get("body"))
