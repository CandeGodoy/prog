def domino(tupla1,tupla2):
    if set(tupla1) & set(tupla2):
        return True
    
    
    
    
    
#-----Programa Principal
    
lista1=[]

for i in range(2):
    num = int(input("Ingrese el valor de la ficha 1"))
    lista1.append(num)

lista2=[]

for i in range(2):
    num = int(input("Ingrese el valor de la ficha 2"))
    lista2.append(num)
    
    
print(domino(tuple(lista1),tuple(lista2)))
