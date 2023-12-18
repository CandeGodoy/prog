#Ejercicio 8

def separar(cadena):
    
    cadenaSep = cadena.split()
    cadenaSep.sort()
    cadenaUnida = ' '.join(cadenaSep)
    
    return cadenaUnida
    

#-------------PROGRAMA PRINCIPAL

cadenaCarac = input('Ingrese palabras: ')
print("Cadena ordenada:",separar(cadenaCarac))