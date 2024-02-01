import random
#------------------------------------------------------
try:
    arch = open("informacion.txt","rt",encoding="utf-8")
    

    numeros = [[i]+[k] for k in ["A","B","C"] for i in range(1,11) ] + [[i]+[k] for k in ["A","B","C","D"] for i in range(1,11) ]

    print("\tPASAJERO\t    FILA\t\tASIENTO")
    colisiones = []
    ocupadosAsiento = []
    ocupadospersona = []
    for linea in arch:
        linea = linea.rstrip("\n")
        pasajero = linea.split(";")
        
        if len(pasajero)!=1:
            ocupadosAsiento.append(pasajero[1:])
            ocupadospersona.append(pasajero[0])
        else:
            asiento = random.choice(numeros)
            numeros.remove(asiento)
            ocupadospersona.append(pasajero[0])
            pasajero= pasajero+asiento
            ocupadosAsiento.append(asiento)
            
        for ll in pasajero:
            print(f"{ll:^20}",end="")
        print()
    libres = [["LIBRE"]+e for e in numeros]
    print("\n")        
    print("\t\t\tASIENTOS LIBRES")
    print("\tPASAJERO\t    FILA\t\tASIENTO")
    for dd in libres:
        for ddd in dd:
            print(f"{ddd:^20}",end="")
        print()
        
    
    print("\n")        
    print("\t\t\tCOLISIONES")
    print("\tPASAJERO\t    FILA\t\tASIENTO")
    while ocupadosAsiento:
        elemento = ocupadosAsiento[0]
        veces = ocupadosAsiento.count(ocupadosAsiento[0]) 
        for co in range(veces):
            pos = ocupadosAsiento.index(elemento)
            colisiones.append([ocupadospersona[pos]]+[str(ocupadosAsiento[pos][0])]+[ocupadosAsiento[pos][1]])
            ocupadosAsiento.pop(pos)
            ocupadospersona.pop(pos)
            
    ordenada = sorted(colisiones,key=lambda x: int(x[1]))

    for t in ordenada:
        for tt in t:
            print(f"{tt:^20}",end="")
        print()

except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass