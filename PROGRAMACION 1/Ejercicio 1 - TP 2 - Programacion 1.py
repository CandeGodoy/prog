import random

def rellenar_lista(lista):
    azar = random.randint(1,5)
    for i in range(azar):
        num_azar = random.randint(1,5)
        lista.append(num_azar)
        
    suma = 0
    for elemento in lista:
        suma +=elemento
    
    return lista , suma

def eliminar(listaAzar,num):
    while num in listaAzar:
        listaAzar.remove(num)
    return listaAzar
    
def capicua(lista2):

    long = len(lista2)
    for j in range(long//2):
        if lista2[j] == lista2[long-j-1]:
            valor = True
        else:
            valor = False
    return valor
        



#-----------PROGRAMA PRINCIPAL

lista_azar = []

lista1, suma1 = rellenar_lista(lista_azar)
print("LISTA", lista1)
print("SUMA",suma1)

numero = int(input("Ingrese el numero a eliminar: "))

print(eliminar(lista_azar,numero))

cande = capicua(lista_azar)
if cande:
    print("CAPICUA")
else:
    print("NO CAPICUA")