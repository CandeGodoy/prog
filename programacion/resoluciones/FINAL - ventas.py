def buscador():
    while True:
        try:
            buscar = int(input("Ingrese un mes: "))
            
            assert 1<=buscar<=12,"Mes invalido"
            
            return buscar
            
        except AssertionError as mensaje:
            print(mensaje)
            
#--------------------

try:
    arch=open("ventas.txt","rt")
    mes = {x:[[0 for f in range(1,16)]]+[[0 for t in range(1,100)]] for x in range(1,13)}
     
    for linea in arch:
        linea = linea.rstrip("\n")
        numero = int(linea[:2].lstrip("0"))
        codigo=int((linea[2:4]).lstrip("0"))
        cantidad = int(linea[4:8].lstrip("0"))
        fecha=int((linea[10:12]).lstrip("0"))
        
        mes[fecha][0][numero-1]+=cantidad
        mes[fecha][1][codigo-1]+=cantidad

    numero1 = buscador()
    
    messss = mes[numero1]
    
    print(("MES:"+str(numero1)).center(30))
    
    print("VENDEDOR\tCANTIDAD")
    for numero,caca in enumerate(messss[0]):
        print(f"{numero+1:^10}{caca:^20}")
    print("\tARTICULO\tCANTIDAD")
    for numero2,caca2 in enumerate(messss[1]):
        print(f"{numero2+1:^5}{caca2:^10}")
            
    
    
    
    
        
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass