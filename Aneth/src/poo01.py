class Producto:
    """Clase producto"""
    def __init__(self,nombre: str,precio: float):
        """Constructor de clase"""
        self.nombre = nombre 
        self.precio = precio

producto_uno = Producto("Pan bimbo",56.99)
print (f"Producto1: {producto_uno.nombre} costo de {producto_uno.precio}")      

#Property y setter

class ProductoSetter:
    """Clase producto"""
    def __init__(self,nombre: str,precio: float):
        """Constructor de clase"""
        self.nombre = nombre 
        self.precio = precio

    @property #Acceder a la propiedad pero son miodificarlo
    def precio(self) ->float:
        # Getter. Nos permite acceder a la propuedad de .precio pero sin pasarle los parentesis
        return self._precio

    @precio.setter
    def precio(self,value: float):
        """Nos permite modificar el valor de la propiedad y aplicar validaciones"""
        if value <=0:
            raise ValueError("El precio debe ser mayor a cero")

        self._precio = value

    def __str__(self) -> str:
        """Metodo especila que nos permite el llamado para convertir a cadena de texto"""
        return (f"El producto {self.nombre} tiene un costo de {self.precio}")



producto_dos = ProductoSetter ("Pan con linaza",32.0)

print(producto_dos)

print(f"Producto 2: {producto_dos.nombre} costo de {producto_dos.precio}")

producto_dos.precio = 89

print(f"Producto 2: {producto_dos.nombre} costo de {producto_dos.precio}")