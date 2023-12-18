import random

def crear_matriz(n,matriz_creada):
    for f in range(n):
        matriz_creada.append([])
        for c in range(n):
            matriz_creada[f].append(0)
            
            
def rellenar_lista(n,lista):
    for i in range(n**2):
        lista.append(i)
    random.shuffle(lista)
    
def rellenar_matriz(n,matriz,lista):
    for f in range(n):
        for c in range(n):
            ele=random.choice(lista)
            matriz[f][c]=ele
            lista.remove(ele)
            
def imprimir_matriz(n,matrizI):
    for fila in matrizI:
        for elemento in fila:
            print("%3d"% elemento, end="")
        print()





#--------PROGRAMA PRINCIPAL

matrizR= []

num = int(input("Ingrese el tamaño de la matriz: "))

listaAzar=[]

crear_matriz(num,matrizR)
rellenar_lista(num,listaAzar)
rellenar_matriz(num,matrizR,listaAzar)
imprimir_matriz(num,matrizR)
