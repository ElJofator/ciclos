# Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
pedir = True
minutos = 0
try:
    while(pedir):
        tramo = int(input("Duración tramo: "))
        if(tramo == 0):
            pedir = False
        else:
            minutos += tramo
    horas = 0
    while(minutos >= 60):
        minutos -= 60
        horas += 1
    if(minutos < 10):
        print(f"Tiempo total de viaje: {horas}:0{minutos} horas")
    else:
        print(f"Tiempo total de viaje: {horas}:{minutos} horas")
except ValueError:
    print("No es un número válido")