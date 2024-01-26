try:
    arch = open("mercaderia.txt","rt")
    
    listaCantidad = []
    listaProducto=[]
    cont=0
    
    for linea in arch:
        linea = linea.strip("\n")
        
        if cont%2==0:
            lista = linea[:10].split()
            lista.append(linea[11:31].strip())
            lista = lista+linea[32:].split()
            if lista[3] not in listaProducto:
                listaProducto.append(lista[3])
                listaCantidad.append(int(lista[4]))
            else:
                pos = listaProducto.index(lista[3])
                listaCantidad[pos]+=int(lista[4])
        else:
            listaV = linea[:14].split()
            listaV.append(linea[15:35].strip())
            listaV = listaV+[linea[36:]]
            if listaV[4] not in listaProducto:
                listaProducto.append(listaV[4])
                listaCantidad.append(-int(listaV[3]))
            else:
                posV = listaProducto.index(listaV[4])
                listaCantidad[posV]-=int(listaV[3])
             
        cont+=1

    
    listaCombinada =[[listaProducto[i],listaCantidad[i]] for i in range(len(listaCantidad))]

    ListaOrdenada = sorted(listaCombinada, key=lambda k: k[1],reverse=False)
    
    print("      PRODUCTO\t\t  Cantidad")
    print("-"*35)
    for fila in ListaOrdenada:
        for elemento in fila:
            print(f"{elemento:^20}",end="")
        print()
    
except FileNotFoundError as mensaje:
    print("Archivo no encontrado: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass