
from Funcion import funcion


def test_1():
    assert funcion(5, 4) != -1


def test_2():
    assert funcion("3", 4) == -1


def test_3():
    assert funcion(3, 4) == -1
