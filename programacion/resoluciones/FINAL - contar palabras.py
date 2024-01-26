def limpiar_palabras(listaL):
    acentos = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u"
        }
    for f in range(len(listaL)):
        listaL[f]=listaL[f].lower()
        for fila in listaL:
            for elem in fila:
                if elem in acentos:
                    listaL[f]=listaL[f].replace(elem,acentos[elem])
        
def repetidos(listaR):
    repetidos = {}
    for elemento in listaR:
        if len(elemento)>3:
            if elemento not in repetidos:
                repetidos[elemento]=0
            if elemento in listaR:
                repetidos[elemento]+=1
    print(repetidos)
    

try:
    arch  = open("frases.txt","rt",encoding="utf-8")
    
    lista = []
    
    
    for linea in arch:
        linea = linea.rstrip("\n")
        lineas = linea.split()
        lista+=lineas
    
    limpiar_palabras(lista)
    print(lista)
    repetidos(lista)
    

    
except FileNotFoundError as mensaje:
    print("Archivo no encontrado: ",mensaje)
except OSError as mensaje:
    print("No se pudo leer el archivo",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass