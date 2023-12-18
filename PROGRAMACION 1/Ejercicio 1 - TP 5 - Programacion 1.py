def verificar():
    while True:
        try:
            numero = int(input("Ingrese un numero natural: "))

            if numero<0:
                raise ValueError("Ingresó un numero menor a 0")
            
            break
            
        except ValueError as mensaje:
            print(mensaje)
            print("Intente nuevamente")
            
    return numero
    
    
    
    
#----------PROGRAMA PRINCIPAL
        
print(verificar())