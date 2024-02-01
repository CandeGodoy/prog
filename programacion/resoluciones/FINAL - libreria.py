try:
    arch = open("pedidos.txt","rt")
    
    articulos ={}
    
    for linea in arch:
        linea = linea.rstrip("\n")
        registro  = linea.split(",")
        
        tupla = (registro[1],registro[0])
        
        mes = int((registro[2][2:4]).lstrip("0"))
        
        if tupla not in articulos:
            articulos[tupla] = [0 for x in range(1,13)]
            articulos[tupla][mes] = int(registro[3])
        else:
            articulos[tupla][mes] += int(registro[3])
            
    print(articulos.items())
    
    ordenada = dict(sorted(articulos.items(),key=lambda x:x[0][1]))
            
            
    for clave,valor in ordenada.items():
        canti,maxi = max(((cant,pos) for pos,cant in enumerate(valor)))
        print("El articulo:",clave[0],"mes:",maxi,"cantidad:",canti)
    
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass