"""Desarrollar una funcion que devuelva el minímo elemento de una matriz M x N"""
import random

def crear_matriz(fila,colum,matrizC):
    for f in range(fila):
        matrizC.append([])
        for c in range(colum):
            matrizC[f].append(0)
            
def rellenar_matriz(fil,col,matrizR):
    for ff in range(fil):
        for cc in range(col):
            numero = random.randint(1,20)
            matrizR[ff][cc]=numero
    
def minimo(matrizMin):
    if len(matrizMin)<=0:
        return matrizMin
    if len(matrizMin)==1:
        return matrizMin[0][0]    
    elif matrizMin[0][0] <= minimo(matrizMin[1:]):
        return matrizMin[0][0]
    else:
        return minimo(matrizMin[1:])

    
            
def imprimir_matriz(matrizI):
    for fff in matrizI:
        for elemento in fff:
            print("%3d"% elemento,end=" ")
        print()


#--------------PROGRAMA PRINCIPAL

matriz = []
columnas = int(input("Ingrese el numero de columnas: "))
filas = int(input("Ingrese el numero de filas: "))

crear_matriz(filas,columnas,matriz)
rellenar_matriz(filas,columnas,matriz)
imprimir_matriz(matriz)
minimoooo = minimo(matriz)
print(f"El mínimo elemento en la matriz es: {minimoooo}")