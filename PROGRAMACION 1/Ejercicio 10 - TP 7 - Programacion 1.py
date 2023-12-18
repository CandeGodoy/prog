import random

def mostrar(matrizM,fila=0,col=0):
    if fila ==(len(matrizM)):
        return 0
    if col == len(matrizM[0]):
        return mostrar(matrizM,fila+1,0)
    return matrizM[fila][col] + mostrar(matrizM,fila,col+1)

    

#-------------------------
matriz=[[1,2,3],
        [4,5,6]]

print(mostrar(matriz))