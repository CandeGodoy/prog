copias = int(input("Ingrese la cant de copias"))
paginas = int(input("Ingrese la cant de paginas"))

sinI = [i for i in range(1,paginas+1) for k in range(copias)]
conI = [c for c in range(copias) for c in range(1,paginas+1)]

print(conI)