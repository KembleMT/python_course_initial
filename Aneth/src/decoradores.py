import time
"""
print("Time", time.time())
sum([i**2 for i in range(100000)])
print("Time", time.time())
"""

def decoraror(func):
    def envoltura():
        print("Inicio")
        func()
        print ("Final")
        return envoltura

@decorador
def saludo():
# print("Inicio")
    print("Hola mundo")
    # print("Final")

saludo()

#Generar decorador que calcule el tiempo de ejecucion de una funcion

def decorador_tiempo_calc(func):
    def wrapper():
        inicio 
