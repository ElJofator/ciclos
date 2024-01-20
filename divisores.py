#Escriba un programa que entregue todos los divisores del número entero ingresado:
try:
    numero = int(input("Ingrese número: "))
    mensaje = ""
    for i in range(1,numero+1):
        if(numero%i == 0):
            mensaje += f"{i} "
    print(mensaje)
except ValueError:
    print("No es un número válido")