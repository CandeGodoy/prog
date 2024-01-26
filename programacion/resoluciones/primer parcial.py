import random

def crear_matriz(m,n,matriz):
    for f in range(m):
        matriz.append([])
        for c in range(n):
            matriz[f].append(0)
            
def rellenar_matriz(mm,nn,matrizR):
    for ff in range(mm):
        for cc in range(nn):
            azar = random.randint(0,9)
            matrizR[ff][cc]=azar
            
def repetidos(matrizRepe):
    lista=[0]*10
    band=0
    for fila in matrizRepe:
        for elementos in fila:
            lista[elementos]+=1
    
    print(lista)
            
    for i in range(len(lista)):
        if band==0 or lista[i]>mayor:
            mayor=lista[i]
            repetido=i
            band=1
            
    valores_mas_comunes=[y for y, frecuencia in enumerate(lista) if frecuencia == mayor]
                
    return repetido,mayor,valores_mas_comunes
            
    
def imprimir_matriz(matrizI):
    for fila in matrizI:
        for elemento in fila:
            print("%3d"%elemento,end="")
        print()
    
    
#------------------
    
matriz1=[]
filas = int(input("Ingrese filas: "))
colum = int(input("Ingrese colum: "))

crear_matriz(filas,colum,matriz1)
rellenar_matriz(filas,colum,matriz1)
print(repetidos(matriz1))
imprimir_matriz(matriz1)