def rellnar_matriz(matrizR):
    impar =1
    par=2
    for f in range(len(matrizR)):
        for c in range(len(matrizR)):
            if f%2==0:
                matrizR[c][f]=impar
                impar+=2
            else:
                matrizR[c][f]=par
                par+=2

def imprimir_matriz(matrizI):
    for fila in matrizI:
        for elemento in fila:
            print("%3d"%elemento,end="")
        print()
        
def recursiva(x,y,matrizRe,lista):
    
    if len(lista)==len(matrizRe)*len(matrizRe):
        return lista
    else:
        lista.append(matrizRe[x][y])
        
    if y == len(matrizRe)-1:
        y=0
        return recursiva(x+1,y,matrizRe,lista)
    else:
        return recursiva(x,y+1,matrizRe,lista)
#-----------

tamaño = int(input("Ingrese el tamaño de la matriz: "))
matriz = [[0]*tamaño for k in range(tamaño)]
lista1=[]

rellnar_matriz(matriz)
imprimir_matriz(matriz)
print(recursiva(0,0,matriz,lista1))

"""def recursiva(matri,f=0,c=0):
    if f==len(matri):
        return []
    if c==(len(matri[0])-1):
        return [matri[f][c]]+recursiva(matri,f+1,0)
    return [matri[f][c]]+recursiva(matri,f,c+1)"""