#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
n1 = int(input("Ingresa un número: "))
mensaje = ""
for i in range(n1+1):
    mensaje += f"{2**i} "
print(mensaje)