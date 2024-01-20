#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:

#π=4(1−1/3+1/5−1/7+…)
# La entrada del programa debe ser un número entero n
#  que indique cuántos términos de la suma se utilizará.

try:
    n = int(input("n: "))
    suma = 0
    signo = 1
    for i in range(1, 2*n + 1, 2):
        suma += signo/i
        signo *= -1
    print(4*suma)
except ValueError:
    print("No es un número válido")