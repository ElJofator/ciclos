#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

try:
    n1 = int(input("Ingresa un número: "))
    print(f"Tabla del {n1}")
    for i in range(1,11):
        print(f"{n1}*{i} = {n1*i}")
except ValueError:
    print("No es un número válido")