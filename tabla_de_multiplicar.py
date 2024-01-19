#Escriba un programa que muestre una tabla de multiplicar como la siguiente:
for i in range(1,11):
    fila = ""
    for k in range(1,11):
        m = i*k
        if(m < 10):
            fila += f"  {m}"
        elif(m < 100):
            fila += f" {m}"
        else:
            fila += f"{m}"
        fila += " "
    print(f"{fila}")