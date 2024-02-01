
def es_primo(num,cont=2):
    if cont==num:
        return True
    elif num%cont==0:
        return False
    return es_primo(num,cont+1)
    
def goldbach(nume,lista):
    conjunto = set()
    
    for l in range(len(lista)):
        for o in range(len(lista)):
            if lista[l]+lista[o]==nume:
                suma = tuple(sorted([lista[l]]+[lista[o]]))
                conjunto.add(suma)
    ordenada = sorted(list(conjunto),key=lambda x:x[0])
    return ordenada


numero = int(input("Ingrese un numero: "))

primos = [x for x in range(2,numero) if es_primo(x) ]

conju = goldbach(numero,primos)

for h in conju:
    print(f"{h[0]:^10} + {h[1]:^10}")