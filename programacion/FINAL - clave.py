import random

def crear_clave(num,matrizC):
    for f in range(4):
        for c in range(3):
            azar = random.choice(num)
            num.remove(azar)
            matriz[f][c] = azar

def mostrar_matriz(matrizM):
    for fila in matrizM:
        for elemento in fila:
            print("%3s"%elemento, end="")
        print()
#----------------------

valores = [x for x in range(10)] + ["#","*"]


matriz= [[0]*3 for i in range(4)]

crear_clave(valores,matriz)

mostrar_matriz(matriz)