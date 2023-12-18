def buscarclave(dicc,valor):
    lista=[]
    for clave,valorr in dicc.items():
        if valor == valorr:
            lista.append(clave)
    return lista



#--------PROGRAMA PRINCIPAL

dic={
    "a":2,
    "b":4,
    "c":2,
    "d":4
    }

numero = int(input("Ingrese valor: "))

print(buscarclave(dic,numero))