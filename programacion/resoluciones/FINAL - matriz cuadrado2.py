
def patron(matrix):
    cont=1
    for f in range(len(matrix)):
        for c in range(f,len(matrix)-f):
            matrix[f][c]=cont
            matrix[c][f]=cont
            matrix[c][len(matrix)-f-1]=cont
            matrix[len(matrix)-f-1][c]=cont
        cont+=1
        

def imprimir(ma):
    for fila in ma:
        for elemento in fila:
            print("%3d"%elemento,end="")
        print()

matriz = [[0]*7 for g in range(7)]

patron(matriz)
imprimir(matriz)