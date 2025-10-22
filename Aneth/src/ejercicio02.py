# fibonacci: Es la secuencia donde cada número es la suma de los dos anteriores
def fibonacci_for(n: int):
    resultados = []
    a, b = 0, 1
    for i in range(n):
        resultados.append(a)
        a, b = b, a + b
    return resultados

# Ejemplo:
for num in fibonacci_for(10):
    print(num, end=" ")
    

def fibonacci_yield(n):
    a, b = 0, 1
    for i in range(a):
        yield i
        a, b = b, a + b

# Ejemplo:
print("\n")
for num in fibonacci_yield(10):
    print(num, end=" ")
