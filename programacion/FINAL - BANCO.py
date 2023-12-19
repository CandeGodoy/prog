#TODO
"""Usé diccionarios porque me pareció la opción mas eficiente para desarrollar el programa
Primero el programa guarda el número de vendedor y va sumando la cantidad de ventas
Luego recurre a las funciones para realizar las debidas búsquedas"""
def obtenercliente(diccionario, buscador):
    if len(str(buscador)) == 1:
        buscador = "0" + str(buscador)
    else:
        buscador = str(buscador)
    if diccionario.get(buscador) == None:
        return ("No se encontró el vendedor")
    else:
        string = (f"El vendedor {buscador} realizó {diccionario.get(buscador)} ventas")
        return string

def search():
    try: 
        while True: 
            buscar = int(input("Ingrese el número de vendedor del cual desee saber sus ventas o -1 para terminar: "))
            if buscar == -1:
                break
            else:
                assert 0 < buscar and buscar < 16, "El número de vendedor debe ser entre 1 y 15. Intente nuevamente"
                busqueda = obtenercliente(dic, buscar)
                print(busqueda)
    except ValueError:
        print("El caracter ingresado no es un número. Intente nuevamente")
        search()
    except AssertionError as mensaje:
        print(mensaje)
        search()

#Programa principal
try:
    archivo = open("ventas.txt")
    dic = {}
    for linea in archivo:
        vendedor = linea[:2]
        cantidad = linea[4:8]
        cantidad = int(cantidad) #Saca los 0 de adelante
        cantidad = str(cantidad)
        if vendedor not in dic:
            dic[vendedor] = 1
        else:
            dic[vendedor] += 1
    search()
except FileNotFoundError:
    print("No se encontró el archivo")
finally:
    try:
        archivo.close()
    except NameError:
        pass