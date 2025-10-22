"""
#Funcion
def saludar (nombre : str)-> str:
 '''Funcion que devuelve un saludo'''
    return f"Hola{nombre}"
print(saludar())

#Funcion con rgumeno por default
def saludo_generico(nombre = "Usuario"):
    return f"Hola{nombre}"

print(saludo_generico("John"))


"""

#lambda
def suma(num1: int, num2: int) -> int:
     '''Suma de dos numeros'''
     return num1 + num2

suma_lambda = lambda n1,n2 : n1 + n2

print (suma(2,3))
print (suma_lambda(2,3))

#Map y flter
"""Un map nos modifica cada elemento de mi lista
    Un filter nos selecciona cada elemento de mi lista
"""

#Map

lista_numeros=[1, 2, 3, 4, 5]

print("Antes de map y de filter")
print(lista_numeros)


set ={1,2,3,4}
print(set)

tipo_dato = tye(map(lambda x: x**2,lista_numeros))
print(f"Tipo de dato{tipo_dato}")

cuadradis = list(map(lambda x: x**2,lista_numeros))
print (cuadrados)

# filter
pares  list (filter(lambda x : x%2 ==0, lista_numeros))
print(pares)