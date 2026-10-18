from src.calculadora import (
    calcular_area_rectangulo,
    calcular_perimetro_rectangulo,
    dividir,
    maximo,
    minimo,
    multiplicar,
    potencia,
    promedio,
    raiz_cuadrada,
    restar,
    sumar,
)
import pytest

def test_sumar_positivos():
    
    # Arrange
    a, b = 7, 5

    # Act
    resultado = sumar(a, b)
    
    # Assert
    assert resultado == 12

def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_raiz_negativa_lanza_error():

     # Arrange 
     a = -25

     # Act + Assert
     with pytest.raises(ValueError):
         raiz_cuadrada(a)

def test_encontrar_minimo():

    # Arrange
    array = [3, 4, 2, 12, 7]

    # Act 
    resultado = minimo(array)

    # Assert
    assert resultado == 2


def test_restar_numeros_negativos():
    # Arrange
    a, b = -4, -9

    # Act
    resultado = restar(a, b)

    # Assert
    assert resultado == 5


@pytest.mark.parametrize(
    "a, b, resultado_esperado",
    [(0, 25, 0), (-3, 4, -12), (2.5, 4, 10)],
)
def test_multiplicar_cubre_cero_negativos_y_decimales(a, b, resultado_esperado):
    # Act
    resultado = multiplicar(a, b)

    # Assert
    assert resultado == resultado_esperado


@pytest.mark.parametrize(
    "base, exponente, resultado_esperado",
    [(5, 0, 1), (2, 3, 8), (4, -1, 0.25)],
)
def test_potencia_cubre_exponente_cero_positivo_y_negativo(
    base, exponente, resultado_esperado
):
    # Act
    resultado = potencia(base, exponente)

    # Assert
    assert resultado == resultado_esperado


def test_promedio_y_maximo_de_lista_con_repetidos():
    # Arrange
    numeros = [7, 2, 7, 4]

    # Act
    resultado_promedio = promedio(numeros)
    resultado_maximo = maximo(numeros)

    # Assert
    assert resultado_promedio == 5
    assert resultado_maximo == 7


@pytest.mark.parametrize(
    "base, altura, area_esperada, perimetro_esperado",
    [(0, 8, 0, 16), (3, 4, 12, 14), (2.5, 4, 10, 13)],
)
def test_rectangulo_calcula_area_y_perimetro(
    base, altura, area_esperada, perimetro_esperado
):
    # Act
    area = calcular_area_rectangulo(base, altura)
    perimetro = calcular_perimetro_rectangulo(base, altura)

    # Assert
    assert area == area_esperada
    assert perimetro == perimetro_esperado


def test_promedio_de_lista_vacia_lanza_error():
    # Act + Assert
    with pytest.raises(ValueError):
        promedio([])