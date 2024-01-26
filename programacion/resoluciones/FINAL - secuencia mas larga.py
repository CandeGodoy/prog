import random

def recursiva(lista1):
    secuencia_larga = []
    secuencia_actual = []
    
    for num in lista1:
        if not secuencia_actual or num>=secuencia_actual[-1]:
            secuencia_actual.append(num)
        else:
            if len(secuencia_actual)>len(secuencia_larga):
                secuencia_larga = secuencia_actual.copy()
                secuencia_actual = [num]
    if len(secuencia_actual)>len(secuencia_larga):
            secuencia_larga = secuencia_actual.copy()
    return secuencia_larga


numero = int(input("Ingrese un numero: "))

lista = [random.randint(0,10) for x in range(numero)]

print(lista)

print(recursiva(lista))