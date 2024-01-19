#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:
def rectangulo():
    altura = int(input("Altura: "))
    ancho = int(input("Ancho: "))
    for i in range(altura):
        mensaje = ""
        for k in range(ancho):
            mensaje += "*"
        print(mensaje)

#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:
def triangulo():
    altura = int(input("Altura: "))
    for i in range(1, altura+1):
        mensaje = ""
        for k in range(i):
            mensaje += "*"
        print(mensaje)

#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
def hexagono():
    lado = int(input("Lado: "))
    for i in range(0, 2*lado - 1):
        mensaje = ""
        adicional = i
        if(i >= lado):
            adicional = 2*lado - 2 - i
        for k in range(1, 3*lado-1):
            if(lado - adicional <= k < 2*lado + adicional):
                mensaje += "*"
            else:
                mensaje += " "
        print(mensaje)
hexagono()