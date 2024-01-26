import random

def crear_matriz(n,matriz):
    for f in range(n):
        matriz.append([])
        for c in range(n):
            matriz[f].append(0)
            
            
def numeros_Azar(cant):
    lista=[]
    for i in range(cant**2):
        azar=random.randint(0,99)
        while azar in lista:
            azar=random.randint(0,99)
        lista.append(azar)
    return lista

def rellenar_matriz(num,matrizR,l):
    indice = 0
    for f in range(num):
        for c in range(num):
            matrizR[f][c]=l[indice]
            indice+=1
    
def suma_diagonal(num1,matrizSum):
    suma=0
    for f in range(num1):
        for c in range(num1):
            if c<f:
                suma+=matrizSum[f][c]
    return suma


def imprimir_matriz(matrizI):
    for fila in matrizI:
        for elemento in fila:
            print("%4d"%elemento,end="")
        print()
            
            
        
#------------PROGRAMA PRINCIPIAL
            
tamaño = int(input("Ingrese el tamaño: "))

matriz1 =[]

crear_matriz(tamaño,matriz1)
listanum = numeros_Azar(tamaño)
rellenar_matriz(tamaño,matriz1,listanum)

imprimir_matriz(matriz1)

print(suma_diagonal(tamaño,matriz1))