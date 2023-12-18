# Ejercicio 2 - TP 3 - Programacion 1
"""Godoy, María Candela - Zeisel, Nina - Casais, Leila - Florindo, Maria Victoria - Nazar, Zahira"""

def CrearMatriz(ff,cc,matrizOrd):
    i=1
    for f in range(ff):
        matrizOrd.append([])
        for c in range(cc):
            if (f%2==0 and c%2==0) or (f%2!=0 and c%2!=0):
                matriz[f].append(0)
            else:
                matriz[f].append(i)
                i+=1
                
    
def imprimirMatriz(matrizImp):
    for f in matrizImp:
        for elemento in f:
            print("%3d"%elemento,end="")
        print()



#------------PROGRAMA PRINCIPAL

filas = int(input("Ingrese el numero de filas: "))
columnas= int(input("Ingrese el numero de columnas: "))
matriz=[]

CrearMatriz(filas,columnas,matriz)
imprimirMatriz(matriz)