
def clave_maestra(cadena):
    clave1 = cadena[1::2]
    clave2 = cadena[0::2]
    return clave1,clave2


#-------PROGRAMA PRINCIPIAL

clave = input("Ingrese la clave maestra: ")

print(clave_maestra(clave))