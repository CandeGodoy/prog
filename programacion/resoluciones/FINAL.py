def limpiar_palabra(palabra):
    letras = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u"
        }
    palabra = palabra.lower()
    for p in palabra:
        if p in letras:
            palabra = palabra.replace(p,letras[p])
    
    limpiar= [c for c in palabra if c.isalpha()]
    return "".join(limpiar)

def justificar(cantidad):
    caca=sum(len(p) for p in cantidad)
        
    espacios = (200-caca)//(len(cantidad)-1)
    resto = (200-caca)%(len(cantidad)-1)
    lineaJus=""
    
    for i,palabra in enumerate(cantidad):
        lineaJus+=palabra
        if i<resto:
            lineaJus +=" "*(espacios+1)
        elif i<(len(cantidad)-1):
            lineaJus +=" "*(espacios)
    return lineaJus

try:
    arch = open("g.txt","rt",encoding="utf-8")
    arch2 = open("justificado.txt","wt")
    
    lineamaslarga = " "
    for linea in arch:
        linea = linea.rstrip("\n")
        
        if len(linea)>len(lineamaslarga):
            lineamaslarga = linea
            
    porcentaje = len(lineamaslarga)*0.8
    caracteres = 0
    caracteres2 = 0
    conjuntoPalabras = set()
    
    arch.seek(0)
    for linea2 in arch:
        linea2 = linea2.rstrip("\n")
        
        caracteres +=len(linea2)
        
        oracion = linea2.split()
        
        for o in range (len(oracion)):
            caracteres2 +=len(oracion[o])
            
            conjuntoPalabras.add(limpiar_palabra(oracion[o]))
            
            
        if len(linea2)>porcentaje and len(linea2)<200:
            arch2.writelines(justificar(oracion)+"\n")
            
    print("La linea mas larga es: ", lineamaslarga)
    print("La cantidad de carac. es: ", caracteres,caracteres2)
    print("La cantidad de palabras es: ", len(conjuntoPalabras))
    listaordenada = sorted(list(conjuntoPalabras),key=lambda x: [len(x),x])
    for c in (listaordenada):
        print(c)
        
except FileNotFoundError as mensaje:
    print("Archivo no encontrado: ",mensaje)
except OSError as mensaje:
    print("ERROR: ",mensaje)
finally:
    try:
        arch.close()
        arch2.close()
    except NameError:
        pass