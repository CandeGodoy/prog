# Ejercicio 2 - TP 3 - Programacion 1
"""Godoy, María Candela - Zeisel, Nina - Casais, Leila - Florindo, Maria Victoria - Nazar, Zahira"""

def generar_matriz(n,matriz1):
    for f in range(n):
        matriz1.append([])
        for c in range(n):
            matriz1[f].append(0)

def RellenarMatriz(fyc,matrizOrd):
    i=1
    for f in range(fyc):
        for c in range(fyc):
            if (f%2==0 and c%2!=0) or (f%2!=0 and c%2==0):
                matrizOrd[f][c]=i
                i+=1
                
    
def imprimirMatriz(matrizImp):
    for f in matrizImp:
        for elemento in f:
            print("%3d"%elemento,end="")
        print()



#------------PROGRAMA PRINCIPAL

filasColum = int(input("Ingrese el numero de filas y columnas: "))
matriz=[]

generar_matriz(filasColum,matriz)
RellenarMatriz(filasColum,matriz)
imprimirMatriz(matriz)