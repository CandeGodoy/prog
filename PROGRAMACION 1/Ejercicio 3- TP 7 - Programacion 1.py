"""Escribir una funcion que devuelva la suma de los N primeros números naturales"""

def sumar(num):
    if num<=1:
        return num
    else:
        return num+sumar(num-1)
    
    


#------------------PROGRAMA PRINCIPAL

numero = int(input("Ingrese un numero: "))

suma = sumar(numero)

print(f"La suma de los {numero} primeros números naturales es: {suma}")


for i in range(numero):
    suma +=i
    
