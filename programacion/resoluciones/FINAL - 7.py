try:
    arch = open("resultados.txt","rt",encoding="utf8")
    dic = {}
    
    for linea in arch:
        linea = linea.rstrip("\n")
        
        partido = linea.split(",")
        
        if partido[0] not in dic:
            dic[partido[0]]=1
        else:
            dic[partido[0]]+=1
            
    lista = sorted(list(dic.items()),key=lambda x: x[1],reverse=True)
    suma = sum(valor for valor in dic.values())
     
    lista4 = {}
    
    arch.seek(0)
    
    for linea2 in arch:
        linea2 = linea2.rstrip("\n")
        par = linea2.split(",")
        
        if par[0]==lista[0][0]:
            if par[1] not in lista4:
                lista4[par[1]]=1
            else:
                lista4[par[1]]+=1
            
    ordenado = sorted(list(lista4.items()),key=lambda x:x[1],reverse=True)
    suma1 = sum(valorr for clave,valorr in lista4.items())      

    for f in range(len(lista)):
        for c in range(len(lista[0])):
            if c!=1:
                print(f"{lista[f][c]:25}",end="")
            else:
                porcentaje = lista[f][c]*100/suma
                total = int(porcentaje/10)
                if total==0:
                    total=1
                print(("*")*total,f"{porcentaje:.2f}%")
                
    print(f"\nPartido ganador: {lista[0][0]}")
    for ff in range(len(ordenado)):
        for cc in range(len(ordenado[0])):
            if cc!=1:
                print(f"Lista {ordenado[ff][cc]:19}",end="")
            else:
                porcentaje = ordenado[ff][cc]*100/suma1
                total = int(porcentaje/10)
                if total==0:
                    total=1
                print(("*")*total,f"{porcentaje:.2f}%")     
        
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass