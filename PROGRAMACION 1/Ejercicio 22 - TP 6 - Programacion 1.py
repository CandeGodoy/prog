def imprimir (matriz):
    filas = len (matriz)
    columnas = len (matriz[0])
    print("          ",end="")
    for x in range(12):
        mess = str(x+1)
        print(f"{mess:6}",end="")
    print("\n","   ","-"*90)
    for f in range (filas):
        fila =str(f+1) 
        print(f"{fila:^4}|",end="")
        for c in range (columnas):
            print ("%6d"%matriz[f][c], end ="")
        print ()

try:
    arch = open("datos.txt","rt")
    matriz = [[0]*12 for i in range(31)]
    
    
    for linea in arch:
        linea = linea.rstrip("\n")
        dia,mes,caida = linea.split(";")
        
        matriz[int(dia)-1][int(mes)-1] = int(caida)
        
    imprimir(matriz)
        
    

except FileNotFound as mensaje:
    print("Archivo no encontrado", mensaje)
except OSError as mensaje:
    print("No se pudo leer el archivo",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass