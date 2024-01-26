"""Crear una función recursiva para crear una nueva cadena que contenga sólo los caracteres 
alfabéticos y espacios de otra cadena. Se espera que lo resuelva mediante una función recursiva.
Desarrollar un programa para ingresar frases hasta que sea vacía y para cada frase mostrar la 
cadena creada con la función recursiva"""


def recursiva(cad):
    if len(cad)==0:
        return cad
    if cad[0].isalpha() or cad[0]==" ":
        return cad[0]+recursiva(cad[1:])
    else:
        return recursiva(cad[1:])



cadena = "Programar en Python 3.11 me encanta!"

print(recursiva(cadena))