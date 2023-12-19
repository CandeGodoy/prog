def rotarcadena(cad, n):
    # Congruencia módulo m
    n = n % len(cad)
    return cad[n:]+cad[:n]

# Programa principal
palabra = input("Ingrese la palabra a rotar a la izquierda: ")
while palabra=="":
    palabra = input("Ingrese la palabra a rotar a la izquierda: ")
cant = int(input("Ingrese el factor de rotación: "))
print(rotarcadena(palabra, cant))