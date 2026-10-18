import pytest

from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_apilado,
    descuento_cumulativo,
    descuento_por_volumen,
)


def test_aplicar_descuento():
    # Arrange
    precio = 200
    porcentaje = 15

    # Act
    resultado = aplicar_descuento(precio, porcentaje)

    # Assert
    assert resultado == 170


@pytest.mark.parametrize(
    "porcentaje, resultado_esperado",
    [(0, 100), (100, 0)],
)
def test_aplicar_descuento_en_porcentajes_limite(porcentaje, resultado_esperado):
    # Act
    resultado = aplicar_descuento(100, porcentaje)

    # Assert
    assert resultado == resultado_esperado


@pytest.mark.parametrize("precio, porcentaje", [(-1, 10), (100, -1), (100, 101)])
def test_aplicar_descuento_rechaza_valores_invalidos(precio, porcentaje):
    # Act + Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_calcular_descuento():
    # Arrange
    precio = 80
    porcentaje = 25

    # Act
    resultado = calcular_descuento(precio, porcentaje)

    # Assert
    assert resultado == 20


@pytest.mark.parametrize("precio, porcentaje", [(-1, 10), (100, -1), (100, 101)])
def test_calcular_descuento_rechaza_valores_invalidos(precio, porcentaje):
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)


def test_calcular_precio_final_aplica_impuesto_sobre_precio_con_descuento():
    # Arrange
    precio = 100
    impuesto = 10
    descuento = 10

    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)

    # Assert
    assert resultado == pytest.approx(99)


@pytest.mark.parametrize(
    "precio, impuesto, descuento",
    [(-1, 10, 0), (100, -1, 0), (100, 10, -1), (100, 10, 101)],
)
def test_calcular_precio_final_rechaza_valores_invalidos(
    precio, impuesto, descuento
):
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


@pytest.mark.parametrize(
    "cantidad, precio_unitario, resultado_esperado",
    [(1, 20, 20), (10, 20, 190), (20, 20, 360), (50, 20, 850), (100, 20, 1600)],
)
def test_descuento_por_volumen_aplica_todos_los_limites(
    cantidad, precio_unitario, resultado_esperado
):
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)

    # Assert
    assert resultado == pytest.approx(resultado_esperado)


@pytest.mark.parametrize("cantidad, precio_unitario", [(-1, 10), (10, -1)])
def test_descuento_por_volumen_rechaza_valores_invalidos(
    cantidad, precio_unitario
):
    # Act + Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)


def test_descuento_cumulativo_aplica_descuentos_en_secuencia():
    # Arrange
    precio = 100
    descuentos = [10, 20]

    # Act
    resultado = descuento_cumulativo(precio, descuentos)

    # Assert
    assert resultado == pytest.approx(72)


def test_descuento_cumulativo_sin_descuentos_devuelve_el_precio():
    # Act
    resultado = descuento_cumulativo(100, [])

    # Assert
    assert resultado == 100


@pytest.mark.parametrize("descuentos", [[-1], [101], [10, 101]])
def test_descuento_cumulativo_rechaza_descuentos_invalidos(descuentos):
    # Act + Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(100, descuentos)


def test_descuento_apilado_suma_los_porcentajes():
    # Arrange
    precio = 100
    descuentos = [10, 20]

    # Act
    resultado = descuento_apilado(precio, descuentos)

    # Assert
    assert resultado == 70


def test_descuento_apilado_rechaza_un_total_superior_al_cien_por_ciento():
    # Arrange
    precio = 100
    descuentos = [60, 50]

    # Act + Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)