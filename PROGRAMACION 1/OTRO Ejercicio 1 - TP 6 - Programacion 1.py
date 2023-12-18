try:
    lista = []
    arch = open("Ejercicio 2 - TP 5 - Programacion 1 - copia.py","rt")
    comillas='"'*3
    comillas2="'"*3
    for linea in arch:
        pos = linea.rfind("#")
        posComilla = linea.find(comillas)
        posComilla2 = linea.find(comillas2)
        if pos !=-1:
            if len(linea[:pos])>0:
                lista.append(linea[:pos])
                lista.append("\n")
        elif posComilla==-1 and posComilla2==-1:
            lista.append(linea)
             
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass
    
try:
    archivo = open("noComentarios.txt","wt")
    archivo = archivo.writelines(lista)
    print("Se ha creado el archivo")
except IOError:
    print("No se pudo crear el archivo")
finally:
    try:
        arch.close()
    except NameError:
        pass
    