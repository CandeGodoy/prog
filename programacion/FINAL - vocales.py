
def recursiva(cad,lis):
    vocales = ["a","e","i","o","u"]
    
    if len(cad)==0:
        return lis
    elif cad[0] in vocales:
        if cad[0] not in lis:
            lis.append(cad[0])
    return recursiva(cad[1:],lis)

    



###############
lista = []

cadena = input("Ingrese una palabra: ")


print(recursiva(cadena,lista))