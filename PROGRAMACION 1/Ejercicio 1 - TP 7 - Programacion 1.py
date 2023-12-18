"""Escribir una funcion que devuelva la cantidad de digitos de un num entero, sin utilizar cadenas"""

def recursiva(num):
    num = abs(num)
    if num//10==0:
        return 1
    return 1 + recursiva(num//10)
    
    
###############
numero = int(input("Ingrese un numero: "))

print(f"El numero {numero} tiene",recursiva(numero),"digitos")