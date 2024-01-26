

oblongo = lambda x,x2=0:True if x2*(x2+1)==x else False if x2>x else oblongo(x,x2+1)

def recursiva(n,n2=0):
    if n2*(n2+1) == n:
        return True
    elif n2>n:
        return False
    return recursiva(n,n2+1)
    

numero = int(input("Ingrese un numero: "))


print(recursiva(numero))

print(oblongo(numero))