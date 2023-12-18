def crearTupla(cad):
    
    cadena = cad.replace("@",".")
    
    separar = cadena.split(".") 
    
    return tuple(separar)


#------------------------------

carac = input("Ingrese su mail: ")

print(crearTupla(carac))