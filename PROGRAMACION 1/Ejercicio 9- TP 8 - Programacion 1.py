
def multiplicar(num):
    
    dic = {x: num*x for x in range(1,13)}
        
    return dic

        
#------PROGRAMA PRINCIPAL

valor = int(input("Ingrese un numero: "))
resultado = multiplicar(valor)

for numero in resultado:
    print(valor,"*",numero,"=",resultado[numero])