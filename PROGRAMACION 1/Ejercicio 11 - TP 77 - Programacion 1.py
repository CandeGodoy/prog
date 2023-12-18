import random

def mostrar(matrizM,fila=0,col=0,mini=None):
    if fila ==(len(matrizM)):
        return mini
    if col == len(matrizM[0]):
        return mostrar(matrizM,fila+1,0,mini)
    if mini==None or matrizM[fila][col]<mini:
        mini=matrizM[fila][col]
    return mostrar(matrizM,fila,col+1,mini)

    

#-------------------------
matriz=[[1,2,3],
        [4,5,6]]

print(mostrar(matriz))