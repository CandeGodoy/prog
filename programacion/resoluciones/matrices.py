def crear_matriz(matrizC,n):
    for f in range(n):
        matrizC.append([])
        for c in range(n):
            matrizC[f].append(0)
            
def crear_matrizA(matrizA):
    cont=1
    fila = len(matrizA)
    
    for f in range(fila):
        for c in range(fila):
            if f==c:
                matrizA[f][c]=cont
                cont +=2
                
def crear_matrizB(matrizB):
    contt=1
    filaa = len(matrizB)
    
    for f in range(filaa):
        for c in range(filaa):
            if f+c == (filaa-1):
                matrizb[f][c]=3**(c)
                
def crear_matrizC(matrizC):
    contt=1
    filaC = len(matrizC)
    num=filaC
    for f in range(filaC):
        for c in range(filaC):
            if f>=c:
                matrizC[f][c]=num
        num -=1
        
def crear_matrizE(matrizE):
    contt=1
    filaE = len(matrizE)
    for f in range(filaE):
        for c in range(filaE):
            if (f+c)%2!=0:
                matrizE[f][c]=contt
                contt+=1
                
def crear_matrizF(matrizF):
    contt=1
    filaF = len(matrizF)
    for f in range(filaF):
        for c in range(filaF-1,-1,-1):
            if f+c>=filaF-1:
                matrizF[f][c]=contt
                contt+=1
        
    
def imprimir_matriz(matrizI):
    for filaa in matrizI:
        for elemento in filaa:
            print("%3d"%elemento, end="")
        print()
    
    
    
    
#-----------
matriz = []
matrizb = []
matrizc = []
matrize = []
matrizf = []
numero = int(input("Ingrese la cantidad: "))



crear_matriz(matriz,numero)
crear_matrizA(matriz)
imprimir_matriz(matriz)
print("\n")
crear_matriz(matrizb,numero)
crear_matrizB(matrizb)
imprimir_matriz(matrizb)
print("\n")
crear_matriz(matrizc,numero)
crear_matrizC(matrizc)
imprimir_matriz(matrizc)
print("\n")
crear_matriz(matrize,numero)
crear_matrizE(matrize)
imprimir_matriz(matrize)
print("\n")
crear_matriz(matrizf,numero)
crear_matrizF(matrizf)
imprimir_matriz(matrizf)