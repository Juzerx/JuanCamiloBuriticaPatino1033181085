
import unittest

from calculadora import sumar, restar, multiplicar, dividir


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


if __name__ == "__main__":
    unittest.main()
