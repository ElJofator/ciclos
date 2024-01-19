#La secuencia de Collatz de un número entero se construye de la siguiente forma:

# si el número es par, se lo divide por dos;
# si es impar, se le multiplica tres y se le suma uno;
# la sucesión termina al llegar a uno.
# La conjetura de Collatz afirma que, al partir desde cualquier número, la secuencia siempre llegará a 1. A pesar de ser una afirmación a simple vista muy simple, no se ha podido demostrar si es cierta o no.

# Usando computadores, se ha verificado que la sucesión efectivamente llega a 1 partiendo desde cualquier número natural menor que 258
# .

# Desarrolle un programa que entregue la secuencia de Collatz de un número entero:

def secuencia_de_collatz():
    n = int(input("n: "))
    secuencia = f"{n} "
    while(n > 0 and n != 1):
        if(n%2 == 0):
            n = int(n/2)
        else:
            n = n*3 + 1
        secuencia += f"{n} "
    print(secuencia)

#secuencia_de_collatz()

# Desarrolle un programa que grafique los largos de las secuencias de Collatz de los números enteros positivos menores que el ingresado por el usuario:
    
def secuencia_de_collatz_2():
    n = int(input("n: "))
    for i in range(1, n + 1):
        secuencia = f"{i} *"
        while(i!= 1):
            if(i%2 == 0):
                i = int(i/2)
            else:
                i = i*3 + 1
            secuencia += "*"
        print(secuencia)

secuencia_de_collatz_2()