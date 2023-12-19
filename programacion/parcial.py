import random

def generar_lista(m):
    lista=[]
    azar = random.randint(1,10)
    for i in range(1,m+1):
        while azar in lista:
            azar = random.randint(1,10)
        lista.append(azar)   
        
    return lista

def ordenar(lista1):
    lista12 = sorted(lista1,key= lambda x: (x // 10) % 10)
    
    return lista12

def concatenar(l):
    nueva=str(l[0])+str(l[-1])
    return nueva
        
        
def divisores(lista43):
    
    listadiv = [x for x in range(1,int(lista43)+1) if int(lista43)%x==0]
    
    return listadiv
    


#--------PROGRAMA PRINCIPAL
    
numero = int(input("Ingrese la cantidad: "))


listaa =generar_lista(numero)
print(*listaa)

print(*ordenar(listaa))
con =concatenar(listaa)
print(con)
print(divisores(con))
