def crear_matriz(n,matriz):
    for f in range(n):
        matriz.append([])
        for c in range(n):
            matriz[f].append(0)
            
def rellenar_matriz(cant,matrizR):
    i=1
    for f in range(cant):
        for c in range(cant):
            if f==c or (f+c)==cant-1:
                matrizR[f][c]=0
            else:
                matrizR[f][c]=i
                i+=1
                if f == f//2:
                    if c<f:
                        matrizR[f][c]=i
                        i+=1
                
    
def imprimir_matriz(matrizI):
    for fila in matrizI:
        for elemento in fila:
            print("%2d"%elemento,end="")
        print()



#--------------PROGRAMA PRINCIPAL


matrizPatron=[]

tamaño = int(input("Ingrese el tamaño de la matriz: "))

crear_matriz(tamaño,matrizPatron)
rellenar_matriz(tamaño,matrizPatron)
imprimir_matriz(matrizPatron)