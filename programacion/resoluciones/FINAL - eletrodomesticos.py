try:
    arch=open("electrodomesticos.txt","rt",encoding="utf8")
    
    productos = {}
    
    for linea in arch:
        linea = linea.rstrip("\n")
        registro = linea.split(";")
        
        mes=int(registro[0].lstrip("0"))
        nombre = registro[1]
        precio = int(registro[2])
        
        if nombre not in productos:
            productos[nombre]=[[0 for f in range(31)]]+ [[precio]]
            
            productos[nombre][0][mes-1] = 1
        else:
            productos[nombre][0][mes-1] += 1
            productos[nombre][1][0] += precio
    
    
    cantidad1 = productos["Termotanque"][0]
    mayor = max(cantidad1)
    valores = ",".join([str(pos+1) for pos,cant in enumerate(cantidad1) if cant==mayor])
    if len(valores)>1:
        print("Los meses",*valores,"tuvieron la mayor produccion:",mayor)
    else:
        print("El mes",valores,"tuvo la mayor produccion:",mayor)
        
    for clave,valor in productos.items():
        suma = sum(valor[0])
        print("Producto:",clave,"promedio:",suma/31)
    
    print( "Lo invertido en lavadoras en el mes es de: ",*productos["Lavadora"][1])
    
        
            
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass