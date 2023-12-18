#Ejercicio 1

def capicua(cadena):
    
    longitud = len(cadena)
    
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - 1 - i]:
            valor = False
        else:
            valor = True

    return valor


#-----------------PROGRAMA PRINCIPAL


cadenaCarac = input("Ingrese una palabra: ")

if capicua(cadenaCarac):
    print('"'+ cadenaCarac +'"', 'es capicua')
else:
    print('"'+ cadenaCarac + '"', 'no es capicua')
