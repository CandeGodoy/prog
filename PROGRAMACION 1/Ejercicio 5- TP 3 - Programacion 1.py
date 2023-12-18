import random

def crear_matriz(fil,col,ma):
    for fila in range(fil):
        ma.append([])
        for c in range(col):
            ma[fila].append("O")
    


def mostrar_butacas(filas,columnas,m):
    print("\tBUTACAS")
    for f in range(filas):
        if f==filas//2:
            print("FILAS",end="  ")
        else:
            print("     ",end="  ")
        for c in range(columnas):
            print("%2s"% m[f][c],end="")
        print()
        
def reservar(a,b,m,s,s2):
    valor=False
    if m[s2][s]=="O":
        m[s2][s]="X"
        valor=True
    return valor
    
def cargar_sala(F,C,matrizz):
    total = F*C
    lista=["O","X"]
    
    for f in range(F):
        for c in range(C):
            azar=random.choice(lista)
            matrizz[f][c]=azar
    
def butacas_libres(fila1,colum1,matriz1):
    cont=0
    for f in range(fila1):
        for c in range(colum1):
            if matriz1[f][c]=="O":
                cont+=1
    return cont


#--------PROGRAMA PRINCIPAL

matriz = []

filas = int(input("Ingrese el numero de filas: "))
butacas = int(input("Ingrese el numero de butacas: "))


crear_matriz(filas,butacas,matriz)
cargar_sala(filas,butacas,matriz)
mostrar_butacas(filas,butacas,matriz)

selec = int(input("Ingrese la butaca seleccionada: "))
selec2 = int(input("Ingrese la fila seleccionada: "))

rese = reservar(filas,butacas,matriz,selec,selec2)

if rese:
    print("Se logró reservar!")
else:
    print("ERROR - no se pudo reservar")
mostrar_butacas(filas,butacas,matriz)

print(butacas_libres(filas,butacas,matriz))
