try:
    arch = open("patentes.txt","rt")
    
    personas = {}
    vehiculos = {}
    
    for linea in arch:
        linea = linea.rstrip("\n")
        informacion = linea.split(";")
        
        informacion[2] = float(informacion[2])
        
        if informacion[1] not in personas:
            personas[informacion[1]] = [1]+[informacion[2]]
        else:
            personas[informacion[1]][0] += 1
            personas[informacion[1]][1] += informacion[2]
        
        vehiculos[informacion[0]] = vehiculos.get(informacion[0],0)+informacion[2]


    print("\t   NOMBRE\t\tDEUDA\t")
    print("-"*50)
    
    for clave,valor in personas.items():
        print(f"{clave:^30}{valor[1]:^10}")
    
    print("\n")
    print("\t   NOMBRE\t\tCANT.VEHICULOS\t")
    print("-"*50)
    
    valores= sorted(personas.items(),key=lambda x: x[1][0],reverse=True)
    
    for elemento in range(len(valores)):
        print(f"{valores[elemento][0]:^30}{valores[elemento][1][0]:^10}")

    print("\n")
        
    print("\t   PATENTE\t\tDEUDA")
    print("-"*50)
    for clave,valor in vehiculos.items():
        print(f"{clave:^30}{valor:^10}")
        
        
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass