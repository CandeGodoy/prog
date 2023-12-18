"""Realizar la implementacion recursiva del metodo de seleccion para ordenar una lista de
numeros enteros. Sugerencia: colocar el elemento mas pequeño en la primera posicion, y
luego ordenar el resto de la lista con una llamada recursiva"""

def ordenar(lista):
    if len(lista) <= 1:
        return lista
    
    min_index = lista.index(min(lista))
    
    lista[0], lista[min_index] = lista[min_index], lista[0]

    return  [lista[0]] + ordenar(lista[1:])    
#-------------PROGRAMA PRINCIPAL

listaNumeros = [2,5,2,7,1,1,8,5,3,9,8,86,4,6]



print(ordenar(listaNumeros))

