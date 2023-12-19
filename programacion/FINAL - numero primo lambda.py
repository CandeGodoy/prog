num = lambda x,cont=2:True if x==cont else False if x%cont==0 else num(numero,cont+1)
    
    
numero=int(input("Ingrese"))


    
print(num(numero))


def recursiva(numero,cont=2):
    if numero==cont:
        return True
    if numero%cont==0:
        return False
    return recursiva(numero,cont+1)

print(recursiva(numero))
    
        
    