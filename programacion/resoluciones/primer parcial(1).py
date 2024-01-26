import random

def rellenar_matriz(matrizR,n):
    for f in range(n):
        for c in range(n):
            azar = random.randint(0,10)
            matrizR[f][c] = azar
            
def imprimir_matriz(matrizI):
    for fila in matrizI:
        for elemento in fila:
            print("%3d"%elemento,end="")
        print()
        
def repetidos(matrizR):
    lista = [0 for x in range(11)]
    
    print(lista)
    for filA in matrizR:
        for element0 in filA:
            if element0 in filA:
                lista[element0]+=1
    print(lista)
                
    mayor = max(lista)
    
    repetido = [indice for indice,valor in enumerate(lista) if valor>=mayor]
    return repetido                
            
#-------------------Program


numero = int(input("Ingrese la cantidad: "))
matriz = [[0]*numero for i in range(numero)]


rellenar_matriz(matriz,numero)
imprimir_matriz(matriz)
print(repetidos(matriz))