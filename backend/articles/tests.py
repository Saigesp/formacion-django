from django.test import TestCase


def funcion_suma_str(a, b):
    return str(a + b)

def funcion_multiplicacion(a, b):
    if a < 0:
        raise ValueError("A no puede ser menor que 0")
    return a * b


class ArticleTestCase(TestCase):

    def setUp(self):
        # poner codigo que se repite al inicio de todos los tests
        pass

    def tearDown(self):
        # poner codigo que se repite al final de todos los tests
        pass

    def numero_test(self, numero):
        # se pueden crear funciones auxiliares
        pass

    def test_funcion_suma_str(self):
        resultado = funcion_suma_str(2, 3)
        self.assertEqual(resultado, '5')

    def test_funcion_multiplicacion(self):
        resultado = funcion_multiplicacion(2, 3)
        self.assertEqual(resultado, 6)
        self.assertTrue(resultado > 0)
        self.assertFalse(resultado > 100)

    def test_funcion_multiplicacion_salta_error_con_a_menor_0(self):
        with self.assertRaises(ValueError):
            # ejecutar funcion que da error
            resultado = funcion_multiplicacion(-1, 10)




