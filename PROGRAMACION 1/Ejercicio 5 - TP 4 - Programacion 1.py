
def filtrar_palabras(n,cadena):
    lista=[]
    
    cadenaSep=cadena.split()
    
    for i in range(len(cadenaSep)):
        if len(cadenaSep[i])>=n:
            lista.append(cadenaSep[i])
            
    unida = " ".join(lista)

    return unida

def filtrar_palabras_filter(n,frase):
    palabras = frase.split()
    palabras_filtradas = filter(lambda palabra: len(palabra) >= n, palabras)
    return ' '.join(palabras_filtradas)

#-------PROGRAMA PRINCIPAL

cadenaC=input("Ingrese una cadena: ")
numero=int(input("Ingrese un numero: "))

print(filtrar_palabras(numero,cadenaC))
print(filtrar_palabras_filter(numero,cadenaC))
