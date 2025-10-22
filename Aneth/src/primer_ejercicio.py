def precio_final(producto: str, precio: int, iva: float) -> str:
    '''Cálculo del precio final de un producto'''
    return f"El precio del {producto} es {(precio * iva) + precio} con IVA"


print(precio_final("chocolate", 20, 0.16))
