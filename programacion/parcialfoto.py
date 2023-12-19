def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

N = int(input("Limite superior: "))

lista = [i for i in range(1,N) if i%7==0 or i%10==7]

print(*lista)



ordenada = sorted(lista,key=suma_digitos)

print(*ordenada)