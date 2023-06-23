import random

lista=[]
lista2=[]

for i in range(10):
    auxLegajo=random.randint(1000,9999)
    lista.append(auxLegajo)
    auxPrecio=random.uniform(100.0,999.0)
    lista2.append(auxPrecio)
    
print(lista)
print(lista2)