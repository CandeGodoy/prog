#Ejercicio 1

def mayor(a,b,c):
    may = -1
    if a>b:
        may = a
        if c>a:
            may = c
    elif b>a:
        may = b
        if c>b:
            may=c
            
    return may
        
        



#------------PROGRAMA PRINCIPAL

n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese un numero: "))
n3=int(input("Ingrese un numero: "))

print(mayor(n1,n2,n3))