import math

def validar_numero(a):
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError("El valor debe ser numerico")

def sumar(a, b):
    validar_numero(a)
    validar_numero(b)
    return a + b


def restar(a, b):
    validar_numero(a)
    validar_numero(b)
    return a - b


def multiplicar(a, b):
    validar_numero(a)
    validar_numero(b)
    return a * b


def dividir(a, b):
    validar_numero(a)
    validar_numero(b)

    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    return a / b


def potencia(a, b):
    validar_numero(a)
    validar_numero(b)
    return a ** b


def raiz_cuadrada(a):
    validar_numero(a)

    if a < 0:
        raise ValueError("No se puede calcular la raiz de un numero negativo")

    return math.sqrt(a)