def extraer_rebanadas(pos,cant,cadena):
    
    subcadena1 = cadena[pos:pos+cant+1]
    
    return subcadena1

def extraer(pos,cant,cadena):
    cadenar=""
    
    for i in range(len(cadena)):
        if i>=pos and i<=pos+cant:
            cadenar += cadena[i]
    return cadenar
    


#-------------PROGRAMA PRINCIPAL

cadenaC=input("Ingrese cadena:D :")
posicion=int(input("Ingrese la posicion: "))
cantidad=int(input("Ingrese la cantidad: "))

print(extraer_rebanadas(posicion,cantidad,cadenaC))
print(extraer(posicion,cantidad,cadenaC))
