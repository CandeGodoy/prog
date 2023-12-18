import random

def mostrar(matrizM,fila=0,col=0):
    if fila ==(len(matrizM)):
        return
    if col == len(matrizM[0]):
        print()
        return mostrar(matrizM,fila+1,0)
    print(matrizM[fila][col],end="\t")
    mostrar(matrizM,fila,col+1)

    

#-------------------------
matriz=[[1,2,3],
        [4,5,6]]

mostrar(matriz)