#El número de Euler, e ≈ 2,71828, puede ser representado como la siguiente suma infinita:

# e=1/0!+1/1!+1/2!+1/3!+1/4!+…
# Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.

# Recuerde que el factorial n! es el producto de los números de 1 a n.
import math

try:
    n = int(input("n: "))
    suma = 1
    anterior = 10000
    resta = 1
    i = 1
    while(resta > 0.0001):
        actual = 1/math.factorial(i)
        suma += actual
        resta = anterior - actual
        anterior = actual
        i += 1
    print(suma)
except ValueError:
    print("No es un número válido")