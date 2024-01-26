
def rellenar_matriz(m):
    cont=1
    for fila in range(len(m)):
        for k in range(fila,len(m)-fila):
            m[fila][k]=cont
        for k in range(fila+1,len(m)-fila):
            m[k][len(m)-1-fila]=cont
        for k in range(fila+1,len(m)-fila):
            m[len(m)-1-fila][len(m)-1-k]=cont
        for k in range(len(m)-2-fila,fila,-1):
            m[k][fila]=cont
        cont+=1
def imprimir_matriz(ma):
    for f in ma:
        for elemento in f:
            print("%3d"%elemento,end="")
        print()

#---------------------------------------------------------
while True:
    try:
        tamaño = int(input("Ingrese el tamaño de la matriz: "))

        matriz = [[0]*tamaño for i in range(tamaño)]
        
        rellenar_matriz(matriz)
        imprimir_matriz(matriz)
        
        break
    except ValueError as mensaje:
        print("Ingrese un numero!")
        
        