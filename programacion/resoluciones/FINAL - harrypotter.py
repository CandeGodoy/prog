def limpiar_palabra(pala):
    pala = pala.lower()
    
    vocales = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u"}
    
    limpia = []
    
    for p in pala:
        if p in vocales:
            limpia.append(vocales[p])
        else:
            limpia.append(p)
            
    return "".join(limpia)

def contar_vocales(palabra,vocales=["a","e","i","o","u"]):
    if len(palabra)==0:
        return 0
    elif palabra[0] in vocales:
        return 1+contar_vocales(palabra[1:],vocales)
    return contar_vocales(palabra[1:],vocales)
    

#-------------------

try:
    arch = open("harryPotter.txt","rt",encoding="utf8")
    arch2 = open("parentesis.txt","wt")
    
    
    for linea in arch:
        linea = linea.rstrip("\n")
        oracion = linea.split()
        
        for o in range(len(oracion)):
            limpiada = limpiar_palabra(oracion[o])
            longitud=len(limpiada)*0.5
            cantidad =contar_vocales(limpiada)
            
            if cantidad>longitud:
                oracion[o]="("+oracion[o]+")"
        
        arch2.write(" ".join(oracion)+"\n")
            
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
        arch2.close()
    except NameError:
        pass