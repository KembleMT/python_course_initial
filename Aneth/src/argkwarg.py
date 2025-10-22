#args

def procesar_datos(*args)-> None:
    """Recibe argumentos prosicionales"""
    """ES una tupla que es una conleecion de datos que no se pueden modificar"""
    print (f"Argumentos : {args}")

procesar_datos(10,50,5,4,2)

#keyword arguments

def procesar_datos_kw(**kwargs)-> None:
    """Recibe argumentos posicionales"""
    print (f"Argumentos : {kwargs}")

procesar_datos(10,50,5,4,2)
procesar_datos_kw(nombre="Jona", status= True)

