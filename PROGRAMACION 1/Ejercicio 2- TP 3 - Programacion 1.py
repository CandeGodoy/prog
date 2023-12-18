def crear_matriz(n,matriz):
    for f in range(n):
        matriz.append([])
        for c in range(n):
            matriz[f].append(0)

def matriz_a(n,matriza):
    i=1
    for fila in range(n):
        for colum in range(n):
            if fila==colum:
                matriza[fila][colum]=i
                i+=2
                
def matriz_b(n,matrizb):

    for fila in range(n):
        for colum in range(n):
            if colum+fila == n-1:
                matrizb[fila][colum]=3**(colum)
                
def matriz_c(n,matrizc):
    num = n
    for fila in range(n):
        for colum in range(n):
            if colum<=fila:
                matrizc[fila][colum]=num
        num=num-1

def matriz_d(n,matrizd):
    num=n-1
    for fila in range(n):
        for colum in range(n):
            matrizd[fila][colum]=2**(num)
        num=num-1
        
def matriz_f(n,matrizf):
    num=1
    for fila in range(n):
        for colum in range(n-1,-1,-1):
            if (fila+colum)>=n-1:
                matrizf[fila][colum]=num
                num+=1

def matriz_g(n,matrizg):
    num=1
    for fila in range(n):
        for colum in range(n):
            if (fila+colum)<=n-2:
                matrizg[fila][colum]=num
                num+=1
            elif(fila+colum)<n-1:
                matrizg[fila][colum]=num
                num+=1






                
def imprimir(n,matrizI):
    for filaa in matrizI:
        for elemento in filaa:
            print("%4d"%elemento,end="")
        print()



#---------------PROGRAMA PRINCIPAL
            
num = int(input("Ingrese: "))
matriz1=[]
matriz2=[]
matriz3=[]
matriz4=[]
matriz5=[]
matriz6=[]

crear_matriz(num,matriz1)
matriz_a(num,matriz1)
imprimir(num,matriz1)
print("\n")
crear_matriz(num,matriz2)
matriz_b(num,matriz2)
imprimir(num,matriz2)
print("\n")
crear_matriz(num,matriz3)
matriz_c(num,matriz3)
imprimir(num,matriz3)
print("\n")
crear_matriz(num,matriz4)
matriz_d(num,matriz4)
imprimir(num,matriz4)
print("\n")
crear_matriz(num,matriz5)
matriz_f(num,matriz5)
imprimir(num,matriz5)
print("\n")
crear_matriz(num,matriz6)
matriz_g(num,matriz6)
imprimir(num,matriz6)