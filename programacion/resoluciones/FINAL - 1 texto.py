"""Eran dos ejercicios, en el primero te daban un archivo de texto donde habían diferentes oraciones en cada linea.
El programa constaba en informar por pantalla cada palabra ordenadas de mayor a menor según largo de la palabra y
a partir de ese largo imprimirlas alfabéticamente sin tener en cuenta tildes, signos
de puntuación, numeros o palabras repetidas . Si la palabra se repite se imprime una sola vez. """
def limpiar_palabra(palabra):
    palabra = palabra.lower()
    vocales = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u"}
    limpia=[]
    for p in palabra:
        if p in vocales:
            limpia.append(vocales[p])
        elif p.isalpha():
            limpia.append(p)
            
    return "".join(limpia)
    
    
    
#-------------
try:
    arch = open("textoejemplo.txt","rt",encoding="utf-8")
    conjunto = set()
    
    for linea in arch:
        linea=linea.rstrip("\n")
        oracion = linea.split()
        
        for o in range(len(oracion)):
            oracion[o]=limpiar_palabra(oracion[o])
            conjunto.add(oracion[o].title())
    
    listaOrdenada = sorted(list(conjunto),key=lambda x:[len(x),x])
    print(listaOrdenada)
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass