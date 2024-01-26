
def sumar_precios(matrix,f=0,c=2):
    if f==len(matrix):
        return 0
    return matrix[f][c]+sumar_precios(matrix,f+1,c)

try:
    arch = open("PRECIOSRELEVADOS.txt","rt",encoding="utf8")
    
    articulos ={}
    
    for linea in arch:
        linea = linea.rstrip("\n")
        articulo = linea.split(";")
        
        if articulo[0] not in articulos:
            articulos[articulo[0]] = [[articulo[2]]+[articulo[3]]+[float(articulo[4])]]
        else:
             articulos[articulo[0]] += [[articulo[2]]+[articulo[3]]+[float(articulo[4])]]
    
    for clave,valor in articulos.items():
        print("PRODUCTO: ",clave)
        lista =list(articulos[clave])
        ordenada = sorted(lista,key=lambda x:x[2],reverse=True)
        cantidad = len(valor)
        suma=sumar_precios(valor)
             
        print("Precio maximo: ",ordenada[0][2],"-","Localidad: ",ordenada[0][0],"-","Provincia: ",ordenada[0][1])
        print("Precio minimo: ",ordenada[-1][2],"-","Localidad: ",ordenada[-1][0],"-","Provincia: ",ordenada[-1][1])
        print("Precio promedio: ","%7.2f"%(suma/cantidad))
        print("\n")
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("NO se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass