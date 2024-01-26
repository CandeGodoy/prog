import random


def crear_matriz(m,f=4,c=5):
    for ff in range(f):
        m.append([])
        for cc in range(c):
            m[ff].append(0)
            
def rellenar_matriz(ma):
    for fff in range(len(ma)):
        for ccc in range(len(ma[0])):
            ma[fff][ccc]=random.randint(0,15)
            
def recursiva(matrix):
    conjunto = set()
    repetidos = set()
    
    for filaa in matrix:
        for elemento in filaa:
            if elemento in conjunto:
                repetidos.add(elemento)
            else:
                conjunto.add(elemento)
                
    return len(repetidos)

            
matriz = []
fila = int(input("Ingrese numero de filas"))
col = int(input("Ingrese numero de columnas"))


crear_matriz(matriz,fila,col)
rellenar_matriz(matriz)

print(recursiva(matriz))
print(matriz)