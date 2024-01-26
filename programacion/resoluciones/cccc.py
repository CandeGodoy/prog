try:
    arch = open("mercaderia.txt","rt")
    
    cosas = {}
    dosmil ={}
    
    for linea in arch:
       linea = linea.rstrip("\n")

       if linea[11:14].isdigit():
           año = linea[6:10]
           cant = int(linea[11:14])
           producto = linea[15:35]
           cosas[producto] = cosas.get(producto,0)-cant
           if año=="2009":
                dosmil[producto] = dosmil.get(producto,0)-cant

       else:
            año = linea[6:10]
            cant = int(linea[32:35])
            producto = linea[11:31]
            cosas[producto] = cosas.get(producto,0)+cant
            if año=="2009":
                dosmil[producto] = dosmil.get(producto,0)+cant
            
    ordenada = sorted(list(cosas.items()),reverse=True)       
    print("\nPRODUCTO\tCANTIDAD")
    print("-"*30)
    for clave,valor in cosas.items():
        print(f"{clave:^30}{valor:^5}")
    print("\n")
    print("2009")
    print("\nPRODUCTO\tCANTIDAD")
    print("-"*30)
    for clavee,valorr in dosmil.items():
        print(f"{clavee:^30}{valorr:^5}")
    

    
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass