#Ejercicio 7

def eliminar(cadena,pos,cant):
    sublista1 = cadena[:pos]
    sublista2 = cadena[pos+cant:]
    resultado = sublista1 + sublista2
    return resultado


#------------PROGRAMA PRINCIPAL

cadenaCarac = input("Ingrese la cadena: ")
posicion = int(input("Ingrese la posicion: "))
cantidad = int(input("Ingrese la cantidad de caracteres: "))

print(eliminar(cadenaCarac,posicion,cantidad))