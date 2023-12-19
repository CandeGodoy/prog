
def insertar(cadena,c):
    nueva1=[i+c for i in cadena]
    nueva = "".join(nueva1)
    return nueva
    

def reemplazar(cadena,c):
    cacdena = cadena.replace(" ",c)
    return cacdena

#----------PROGRAMA PRINCIPIAL

cadenaC = input("Ingrese la cadena: ")
carac = input("Ingrese el carac a insertar: ")

print(len(cadenaC))
print(*insertar(cadenaC,carac))
print(reemplazar(cadenaC,carac))