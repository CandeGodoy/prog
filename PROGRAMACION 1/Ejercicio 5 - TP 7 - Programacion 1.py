"""Realizar una funcion que devuelva el resto de dos numeros enteros, utilizando restas sucesivas"""
def resto(num,num1):
    if (num-num1)<num1:
        return num-num1
    else:
        return resto(num-num1,num1)




################
numero = int(input("Ingrese"))
numero1 = int(input("Ingrese"))


print(resto(numero,numero1))
