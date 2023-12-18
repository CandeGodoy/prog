

#-----------

frase = input("Ingrese frase")

lista = frase.split()

conjunto = set(lista)

lista2 = sorted(conjunto,key=lambda x: len(x))

print(lista2)