def limpiar_palabra(palabra):
    palabra=palabra.lower()
    vocales = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u",
        "ñ":"n"}
    limpia = []
    for p in palabra:
        if p in vocales:
            limpia.append(vocales[p])
        elif p.isalpha():
            limpia.append(p)
            
    return limpia
try:
    arch = open("anagramas.txt","rt",encoding="utf-8")
    dic = {}
    
    for linea in arch:
        linea=linea.rstrip("\n")
        oracion = linea.split()
        
        for o in range(len(oracion)):
            if len(oracion[o])>1:
                limpiada = "".join(sorted(limpiar_palabra(oracion[o])))
                oracion[o]="".join(limpiar_palabra(oracion[o]))
                
                if limpiada not in dic:
                    dic[limpiada]={oracion[o]}
                else:
                    dic[limpiada].add(oracion[o])
                    
                  
    lista = sorted(list(dic.values()),key=lambda x:len(x))
    
    for valor in lista :
        if len(valor)>1:
            anagramas=",".join(valor)
            print(anagramas)

        
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass