try:
    arch = open("zen.txt","rt",encoding="utf-8")
    arch2 = open("palabras_largas.txt","wt")
    
    
    palabrasLargas=[]
    for linea in arch:
        palaLarga = " "
        longitud=0
        linea = linea.rstrip("\n")
        palabras = set(linea.split())
        
        for palabra in palabras:
            longitudP = len(set(palabra))
            if longitudP>longitud:
                palaLarga = palabra
                longitud=longitudP
        palabrasLargas.append(palaLarga)
    i=0
    arch.seek(0)
    for linea2 in arch:
        linea2 = linea2.rstrip("\n")
        palabras2 = set(linea2.split())
        palaLarga2 = " "
        
        
        for palabra in palabras2:
            longitudLarga = len(palabrasLargas[i])
            longitudPP = len(set(palabra))
            if palabra not in palabrasLargas and longitudPP==longitudLarga:
                palabrasLargas[i]+=";"+palabra
        i+=1
    for p in palabrasLargas:
        arch2.write(p+"\n")

except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("ERROR: ",mensaje)
finally:
    try:
        arch.close()
        arch2.close()
    except NameError:
        pass