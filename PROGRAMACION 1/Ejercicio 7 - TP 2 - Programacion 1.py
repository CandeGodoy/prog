def rellenar_listas(lista):
    num = int(input("Ingrese: "))
    while num!=-1:
        lista.append(num)
        num = int(input("Ingrese: "))
    return lista

def intercalacion(a,b):

    for i in range(len(a)):
        k=i*2+1
        a[k:k]=[b[i]]
    return a
        





#---------PROGRAMA PRINCIPAL

lista1=[]
lista2=[]

rellenar_listas(lista1)
rellenar_listas(lista2)
print(intercalacion(lista1,lista2))