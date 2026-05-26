from pagos import procesar_pago

def test_pago_exitoso():

    # Arrange
    monto = 100

    # Act
    resultado = procesar_pago(monto)

    # Assert
    assert resultado is True