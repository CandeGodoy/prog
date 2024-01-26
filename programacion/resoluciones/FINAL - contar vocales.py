"""Desarrollar una función recursiva para retornar una lista que contenga solo las vocales de una palabra 
que recibe por parámetro. Las vocales no deben estar repetidas en la lista"""

def limpiar_palabra(pala):
    pala = pala.lower()
    vocales = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u"}
    limpia =[]
    for p in pala:
        if p in vocales:
           limpia.append(vocales[p])
        elif p.isalpha():
            limpia.append(p)
    
    return "".join(limpia)

def recursiva(palab,lista=["a","e","i","o","u"]):
    if len(palab)==0:
        return []
    if palab[0] in lista:
        lista.remove(palab[0])
        return [palab[0]]+recursiva(palab[1:],lista)
    else:
        return recursiva(palab[1:],lista)
    
#--------------------------------
            
            
palabra = input("Ingrese una palabra: ")

palabra = limpiar_palabra(palabra)
print(palabra)
print(recursiva(palabra))