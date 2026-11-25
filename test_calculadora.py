
import unittest

from calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)

    def test_restar(self):
        self.assertEqual(restar(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)

    def test_dividir(self):
        self.assertEqual(dividir(20, 4), 5)

    def test_dividir_entre_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_potencia_exponente_cero(self):
        self.assertEqual(potencia(5, 0), 1)

    def test_raiz_cuadrada(self):
        self.assertEqual(raiz_cuadrada(25), 5)

    def test_raiz_cuadrada_negativa(self):
        with self.assertRaises(ValueError):
            raiz_cuadrada(-9)

    def test_sumar_con_texto(self):
        with self.assertRaises(TypeError):
            sumar("5", 3)

    def test_multiplicar_con_texto(self):
        with self.assertRaises(TypeError):
            multiplicar(5, "3")

if __name__ == "__main__":
    unittest.main()
