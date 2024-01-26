triangular= lambda x,cont=0,i=1: True if cont==x else False if cont>x else triangular(x,cont+i,i+1)

def trianmg(num,cont=0,i=1):   
    if cont==numero:
        return True
    if cont>numero:
        return False
    return trianmg(num,cont+i,i+1)
    
    
    
numero = int(input("Ingrese un numero: "))


print(triangular(numero))