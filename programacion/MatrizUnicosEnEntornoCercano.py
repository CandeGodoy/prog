import random

def llenarmatriz(mat):
    """ Rellena la matriz con números al azar entre 0 y 25
        que sean únicos en su entorno cercano """
    filas = len(mat)
    columnas = len(mat[0])
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            # Construimos una lista con los elementos que rodean a la casilla f,c
            entorno = []
            for ff in range(-1, 2):  # -1, 0, 1. Se usarán como desplazamientos
                for cc in range(-1, 2):
                    # Verificamos no salirnos de la matriz al construir la lista
                    if f+ff>=0 and f+ff<filas and c+cc>=0 and c+cc<columnas:
                        entorno.append(mat[f+ff][c+cc])
            # Verificamos la presencia del número en el entorno que rodea la casilla f,c
            candidato = random.randint(0,25)
            while candidato in entorno:
                candidato = random.randint(0,25)
            # Ahora que encontramos un número que no esté presente, lo cargamos en la matriz
            mat[f][c] = candidato

def imprimirmatriz(mat):
    """ Imprime la matriz mediante recorrido de secuencias """
    print()
    for f in mat:
        for c in f:
            print("%3d" %c, end="")
        print()
    print()

# Programa principal
filas = int(input("Cantidad de filas? "))
columnas = int(input("Cantidad de columnas? "))
# Rellenamos la matriz con -1 porque 0 es parte del intervalo de los números al azar
matriz = [[-1] * columnas for i in range(filas)]
llenarmatriz(matriz)
imprimirmatriz(matriz)
