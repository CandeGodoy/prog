
def espandigital(n):
    num = str(n)
    
    listaNum=[str(i) for i in range(0,10)]

    valor=True
    for f in listaNum:
        if f not in num:
            valor=False
            
    return valor
        
numerooooooo = input("InGRESE")      
        
print(espandigital(numerooooooo))