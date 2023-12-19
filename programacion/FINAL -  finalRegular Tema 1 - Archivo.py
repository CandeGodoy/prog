try:
    arch = open("alumnos.txt","rt")
    arch2 = open("aprobados.txt","wt")
    arch3 = open("desaprobados.txt","wt")
    
    for linea in arch:
        linea=linea.rstrip("\n")
        lista = linea.split(";")
        lista[1]=lista[1].title()
        lista[2]=lista[2].title()
        linea=";".join(lista)
        
        if int(lista[3])>=4 and int(lista[4])>=4:
            arch2.writelines(linea+"\n")
        elif int(lista[3])<4 and int(lista[4])>=4:
            arch3.writelines(linea+";PRIMERO"+"\n")
        elif int(lista[3])>=4 and int(lista[4])<4:
            arch3.writelines(linea+";SEGUNDO"+"\n")
        else:
            arch3.writelines(linea+";AMBOS"+"\n")
    
    
except FileNotFoundError as mensaje:
    print("Archivo no encontrado: ",mensaje)
except OSError as mensaje:
    print("ERROR: ",mensaje)
finally:
    try:
        arch.close()
        arch2.close()
        arch3.close()
    except NameError:
        pass
    