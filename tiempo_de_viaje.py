# Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
bandera = True
minutos = 0
while(bandera):
    tramo = int(input("Duración tramo: "))
    if(tramo == 0):
        bandera = False
    else:
        minutos += tramo
horas = 0
while(minutos >= 60):
    minutos -= 60
    horas += 1
print(f"Tiempo total de viaje: {horas}:{minutos} horas")