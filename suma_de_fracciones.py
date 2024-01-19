#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:

# 1/2,1/4,1/8,1/16,1/32,1/64,…
# en forma decimal:

# 0.5,0.25,0.125,0.0625,0.03125,0.015625,…
# El programa debe mostrar tres columnas que contengan la siguiente información:
#Potencia  Fraccion  Suma
# 1         0.5       0.5
# 2         0.25      0.75
# 3         0.125     0.875
# 4         0.0625    0.9375
# ...       ...       ...
# El programa debe terminar cuando la fracción decimal sea menor o igual a 0.000001.
actual = 1
print("Potencia\tFracción\t\t\tSuma")
potencia = 1
acumulado = 0
while(actual > 0.000001):
    actual = 2**(-potencia)
    print(f"{potencia}\t\t{actual}\t\t\t\t{acumulado + actual}")
    acumulado = actual
    potencia += 1