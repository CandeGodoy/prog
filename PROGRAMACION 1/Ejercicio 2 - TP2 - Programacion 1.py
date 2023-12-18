import random

def generar(lista):
    for i in range (5):
        azar = random.randint(1,10)
        lista.append(azar)
        
        
def repetidos(lista1):
    valor = False
    for j in range(len(lista1)):
        if lista1[j] in lista1[j+1:]:
            valor = True
            
    return valor

def unicos(lista3):
    lista4=[]
    for k in range(len(lista3)):
       if lista3[k] not in lista4:
           lista4.append(lista3[k])
    return lista4

def imprimir(lista5):
    long = len(lista5)
    for f in range(2):
        print(lista5[long-f-1],end=" ")
    
    
#-----------PROGRAMA PRINCIPIAL
    
lista_azar = []


generar(lista_azar)

print(*lista_azar)

if repetidos(lista_azar):
    print("HAY REPETIDOS")

print(*unicos(lista_azar))

imprimir(lista_azar)