# Ejercicio 2 - TP 3 - Programacion 1
"""Godoy, María Candela - Zeisel, Nina - Casais, Leila - Florindo, Maria Victoria - Nazar, Zahira"""

def CrearMatriz(fyc,matrizOrd):
    i=1
    for f in range(fyc):
        matrizOrd.append([])
        for c in range(fyc):
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

filasColum = int(input("Ingrese el numero de filas y columnas: "))
matriz=[]

CrearMatriz(filasColum,matriz)
imprimirMatriz(matriz)