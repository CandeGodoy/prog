#Ejercicio 7 (Sin rebanadas)

def eliminar(cadena,pos,cant,cadena_resul):
    for i in range(len(cadena)):
        if i < pos or i >= pos + cant:
            cadena_resul += cadena[i]
    
    return cadena_resul
        


#------------PROGRAMA PRINCIPAL

cadenaCarac = input("Ingrese: ")
cadenaNueva = ""
posicion = int(input("Ingrese la posicion: "))
cantidad = int(input("Ingrese la cantidad de caracteres: "))

print(eliminar(cadenaCarac,posicion,cantidad,cadenaNueva))