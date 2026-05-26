def calcular_total(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(total):
    if total >= 100:
        return total * 0.9
    return total

def validar_stock(stock, cantidad):
    return stock >= cantidad