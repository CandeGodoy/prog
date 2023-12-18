def contarvocales(palabra):
    vocales = {
        "a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0
        }
    for letra in palabra:
        if letra.lower() in vocales:
            vocales[letra.lower()] +=1
    return vocales

#----

frase = input("Ingrese una frase: ")

separar = frase.split()

for linea in separar:
    print("La palabra ",linea,"tiene ",contarvocales(linea))
    