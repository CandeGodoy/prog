#Ejercicio 5 - TP 2 - Programacion 1
"""Godoy, María Candela - Zeisel, Nina - Casais, Leila - Florindo, Maria Victoria - Nazar, Zahira"""

def lista_ordenada(lista):
    ordenada = True
    for i in range (len(lista)-1):
        if lista[i] > lista[i+1]:
                ordenada = False
    return ordenada

#-------- PROGRAMA PRINCIPAL

lista1 = []

elemento = input("Ingrese numeros o letras - Para finalizar, -1:")
while elemento != "-1":
    lista1.append(elemento)
    elemento = input("Ingrese numeros o letras - Para finalizar, -1:")
    
print(lista_ordenada(lista1))