from ventas import aplicar_descuento

def test_aplicar_descuento():

    # Arrange
    total = 200

    # Act
    resultado = aplicar_descuento(total)

    # Assert
    assert resultado == 180

from ventas import validar_stock

def test_validar_stock():

    # Arrange
    stock = 10
    cantidad = 5

    # Act
    resultado = validar_stock(stock, cantidad)

    # Assert
    assert resultado is True