# Ejercicio 6 - TP 2 - Programacion 1
"""Godoy, María Candela - Zeisel, Nina - Casais, Leila - Florindo, Maria Victoria - Nazar, Zahira"""
def normalizar (lista,lista2):
    total = sum(lista)
    for i in range (len(lista)):
        elemento = lista[i] / total
        lista2.append(elemento)
    return lista2

#---- PROGRAMA PRINCIPAL

Numeros = []
ListaNor = []

elemento = int(input("Ingrese un numero - Para finalizar, -1:"))
while elemento != -1:
    Numeros.append(elemento)
    elemento = int(input("Ingrese un numero - Para finalizar, -1:"))
    
print(normalizar(Numeros,ListaNor))
