"""Desarrollar una función recursiva para buscar el elemento mayor par de la lista, si no existe debe retornar 
-1, Recuerde que se espera la solución recursiva a este problema."""


def recursiva(lista,mayor=-1):
    if len(lista)==0:
        return mayor
    if lista[0]>mayor and lista[0]%2==0:
        mayor = lista[0]
    return recursiva(lista[1:],mayor)




listaN = [1,3,5,7]

print(recursiva(listaN))