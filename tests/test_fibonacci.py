import pytest

from src.fibonacci import (
    es_cuadrado_perfecto,
    es_fibonacci,
    fibonacci_iterativo,
    fibonacci_recursivo,
    fibonacci_serie,
)


@pytest.mark.parametrize(
    "n, resultado_esperado",
    [(0, 0), (1, 1), (2, 1), (5, 5), (10, 55)],
)
def test_fibonacci_iterativo(n, resultado_esperado):
    # Act
    resultado = fibonacci_iterativo(n)

    # Assert
    assert resultado == resultado_esperado


@pytest.mark.parametrize(
    "n, resultado_esperado",
    [(0, 0), (1, 1), (2, 1), (5, 5), (10, 55)],
)
def test_fibonacci_recursivo(n, resultado_esperado):
    # Act
    resultado = fibonacci_recursivo(n)

    # Assert
    assert resultado == resultado_esperado


@pytest.mark.parametrize("funcion", [fibonacci_iterativo, fibonacci_recursivo])
def test_fibonacci_rechaza_indices_negativos(funcion):
    # Act + Assert
    with pytest.raises(ValueError):
        funcion(-1)


@pytest.mark.parametrize(
    "n, resultado_esperado",
    [(0, [0]), (1, [0, 1]), (2, [0, 1, 1]), (6, [0, 1, 1, 2, 3, 5, 8])],
)
def test_fibonacci_serie(n, resultado_esperado):
    # Act
    resultado = fibonacci_serie(n)

    # Assert
    assert resultado == resultado_esperado


def test_fibonacci_serie_rechaza_indices_negativos():
    # Act + Assert
    with pytest.raises(ValueError):
        fibonacci_serie(-1)


@pytest.mark.parametrize(
    "numero, resultado_esperado",
    [
        (-1, False),
        (0, True),
        (1, True),
        (2, True),
        (3, True),
        (4, False),
        (8, True),
        (10, False),
    ],
)
def test_es_fibonacci(numero, resultado_esperado):
    # Act
    resultado = es_fibonacci(numero)

    # Assert
    assert resultado is resultado_esperado


@pytest.mark.parametrize(
    "numero, resultado_esperado",
    [
        (-1, False),
        (0, True),
        (1, True),
        (4, True),
        (9, True),
        (15, False),
    ],
)
def test_es_cuadrado_perfecto(numero, resultado_esperado):
    # Act
    resultado = es_cuadrado_perfecto(numero)

    # Assert
    assert resultado is resultado_esperado


def test_fibonacci_iterativo_y_recursivo_coinciden_en_un_indice_mayor():
    # Arrange
    n = 20

    # Act
    resultado_iterativo = fibonacci_iterativo(n)
    resultado_recursivo = fibonacci_recursivo(n)

    # Assert
    assert resultado_recursivo == resultado_iterativo
