
def zig_zag(matrix):
    cont=1
    for f in range(len(matrix)):
        if f%2==0:
            for c in range(len(matrix[0])):
                matrix[f][c]=cont
                cont+=1
        else:
            for c in range(-1,-len(matrix[0])-1,-1):
                matrix[f][c]=cont
                cont+=1

def imprimir_matriz(matr):
    for fila in matr:
        for elemento in fila:
            print("%3d"%elemento,end="")
        print()

columnas = int(input("Ingrese numero columnas: "))
filas = int(input("Ingrese numero filas: "))

matriz = [[0]*columnas for x in range(filas)]

zig_zag(matriz)
imprimir_matriz(matriz)