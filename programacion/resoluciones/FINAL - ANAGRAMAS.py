import re

def son_anagramas(cadena1, cadena2):
    # Eliminar espacios y signos de puntuación, convertir a minúsculas y quitar vocales con tilde
    cadena1 = re.sub(r'[^a-zA-Z]', '', cadena1).lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    cadena2 = re.sub(r'[^a-zA-Z]', '', cadena2).lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

    # Verificar si las cadenas resultantes son anagramas
    return sorted(cadena1) == sorted(cadena2)

# Programa principal
cadena_1 = input("Ingrese la primera cadena: ")
cadena_2 = input("Ingrese la segunda cadena: ")

if son_anagramas(cadena_1, cadena_2):
    print("¡Son anagramas!")
else:
    print("No son anagramas.")
