from src.calculadora import sumar, dividir, raiz_cuadrada, minimo
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
    assert resultado == 1