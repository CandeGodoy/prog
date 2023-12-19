import random

def crear_matriz(matriz):
    for f in range(4):
        matriz.append([])
        for c in range(3):
            matriz[f].append(0)
            
def rellenar_matriz(matriz_r,listaN):
    for f in range(4):
        for c in range(3):
            pos = random.choice(listaN)
            matriz_r[f][c]=pos
            listaN.remove(pos)
            
def imprimir_matriz(matrizI):
    for fila in matrizI:
        for elemento in fila:
            print("%3s"%elemento,end="")
        print()
        


#-------------
        
matrizContraseña = []
lista = [str(i) for i in range(0,10)]+["#","*"]

print(lista)

crear_matriz(matrizContraseña)
rellenar_matriz(matrizContraseña,lista)
imprimir_matriz(matrizContraseña)