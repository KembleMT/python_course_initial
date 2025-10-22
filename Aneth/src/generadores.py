#yield

def conteo_to_limit(limit: int):
    """Contea desde cero hasta el limite"""
    print("Inicio de funcion tradicional")
    list=[]
    for i in range(limit):
        print("En la poscion",i)#preferible usar f-string
        list.append(i)
        print("Finalia la funcion tradicional")
        return list

def conteo_gen(limit: int):
    print("Inicio del generador")
    for i in range(limit):
        print("En la poscion",i)
    yield i
    print ("Fin del generador")


conteo_to_limit(10)
print(type(conteo_gen(10)))
print(type(conteo_to_limit(10)))

for numero in conteo_to_limit(5):
    print("En tradicional",numero)

for numero in conteo_gen(5):
    print("En generador",numero)
