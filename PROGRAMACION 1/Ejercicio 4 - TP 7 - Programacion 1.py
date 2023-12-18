"""Desarrollar una funcion que devuelva el producto de dos numeros enteros por sumas sucesivas"""
def mul_recursiva(num1,num2):
    if num2==0:
        return 0
    else:
        return num1+mul_recursiva(num1,num2-1)



############
numero = int(input("Ingrese"))
numero1 = int(input("Ingrese"))

print(mul_recursiva(numero,numero1))