import random

def crear_matriz(n,matriz):
    for f in range(n):
        matriz.append([])
        for c in range(n):
            matriz[f].append(0)


def rellenar_matriz(num,matriz_rell):
    for f in range(num):
        for c in range(num):
            azar = int(input("Ingrese num:"))
            matriz_rell[f][c] = azar
            
def suma_magica(cant,matriz_suma):
    valor= False
    suma = sum(matriz_suma[0])
    sumaD1=0
    sumaD2=0
    
    for f in matriz_suma:
        if sum(f) == suma:
            valor = True
        else:
            valor= False
            
    for c in matriz_suma:
        if sum(c) == suma:
            valor = True
        else:
            valor= False
    
    for f in range(cant):
        for c in range(cant):
            if f==c:
                sumaD1+=matriz_suma[f][c]
            elif (f+c)==cant-1:
                sumaD2+=matriz_suma[f][c]
            
    if sumaD1 == suma and sumaD2 == suma:
        valor = True
    else:
        valor= False
    
    return valor,suma

def imprimir_matriz(matriz_imp):
    for fila in matriz_imp:
        for elemento in fila:
            print("%3d"%elemento,end="")
        print()
            
#---------PROGRAMA PRINCIPAL
            
matriz_magica = []

tamaño = int(input("Ingrese el tamaño de la matriz: "))


crear_matriz(tamaño,matriz_magica)
rellenar_matriz(tamaño,matriz_magica)
valorM,sumaM = suma_magica(tamaño,matriz_magica)

if valorM:
    print("Cuadrado mágico con suma",sumaM)
else:
    print("No es cuadrado magico")
imprimir_matriz(matriz_magica)