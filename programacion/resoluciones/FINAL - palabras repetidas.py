def limpiar_palabra(palabra):
    palabra = palabra.lower()
    vocales = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u"}
    limpia = []
    for p in palabra:
        if p in vocales:
            limpia.append(vocales[p])
        elif p.isalpha():
            limpia.append(p)
            
    return "".join(limpia)

#-----------------------------------------------------------

try:
    arch = open("textoejemplo.txt","rt",encoding="utf-8")
    
    palabras = {}
    
    for linea in arch:
        linea = linea.rstrip("\n")
        oracion = linea.split()
        
        for o in range(len(oracion)):
            if len(oracion[o])>3:
                oracion[o]=limpiar_palabra(oracion[o])
                palabras[oracion[o]] = palabras.get(oracion[o],0)+1
            
    listaPalabras = sorted(list(palabras.items()),key=lambda x:[len(x[0]),x[0]])         
    
    print("       PALABRA\t\tREPETICIONES")
    for l in listaPalabras:
        for elemento in l:
            print(f"{elemento:^20}",end="")
        print()
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass