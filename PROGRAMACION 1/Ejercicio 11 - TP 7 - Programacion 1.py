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
    
def minimoElemento(matrizMin,minimo = None):
    
    if len(matrizMin)<=0:
        return minimo
    
    fila = matrizMin[0]
    minFila = min(fila)
    if minimo == None or minFila < minimo:
        minimo = minFila
    return minimoElemento(matrizMin[1:],minimo)

    
            
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
minimoooo = minimoElemento(matriz)
print(f"El mínimo elemento en la matriz es: {minimoooo}")