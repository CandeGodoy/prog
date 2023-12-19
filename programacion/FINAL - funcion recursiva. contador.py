"""Desarrollar un programa para generar un conjunto(set) con numeros enteros obtenidos al azar,
en un rango entre 0 y 1000.Finalizar la carga cuando se genere un numero de valor 0, el que no se
cargará al conjunto. Luego se solicita escribir una funcion recursiva para eliminar todos los elementos
del mismo, informando la cantidad de elementos que este tenia. Mostrar este nmero por pantalla"""

import random


def eliminar(con):
    if len(con)==0:
        return 0
    else:
        con.pop()
    return 1+eliminar(con)


#----------------Programa principal
conjunto = set()

numero = random.randint(0,10)

while numero !=0:
    conjunto.add(numero)
    numero = random.randint(0,10)
    
print(conjunto)
    
print(eliminar(conjunto))