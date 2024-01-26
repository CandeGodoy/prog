

def limpiar_palabra(pala):
    pala = pala.lower()
    vocales= {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u"}
    limpia = []
    for pa in pala:
        if pa in vocales:
            limpia.append(vocales[pa])
        elif pa.isalpha():
            limpia.append(pa)
            
    return limpia


try:
    condicion = True
    while condicion:
        arch = open("palabras.txt","rt")
        
        for linea in arch:
            linea = linea.rstrip("\n")
            intentos = 0
            guiones = ["_"]*len(linea)
            
            palabra = limpiar_palabra(linea)
            print(palabra)
            
            while intentos<=6 and guiones!=palabra:
                letra = (input("Ingrese una letra: ")).lower()
                if letra in palabra:
                    for i in range(len(palabra)):
                        if palabra[i] == letra:
                            guiones[i]=letra
                    
                    print(*guiones)
                else:
                    print(letra,"no se encuentra en la palabra:",guiones)
                    intentos +=1

            valor = input("Si desea seguir jugando escriba SI")
            if valor.upper()=="NO":
                condicion = False
                break
            
            
        
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass
    