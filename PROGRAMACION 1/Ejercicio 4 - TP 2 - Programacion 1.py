
def rellenar_lista(listaR):
    texto = input("Ingrese: ")
    while texto!="a":
        listaR.append(texto)
        texto = input("Ingrese: ")
    return listaR
    
def eliminar(lista,lista1,lista3):
    for elemento in lista:
        if elemento not in lista1:
            lista3.append(elemento)
    
    
    
    
    
    
    
    
#-----------PROGRAMA PRINCIPAL
    
listaC = []
listaC2=[]
listaC3=[]

rellenar_lista(listaC)
print(listaC)
rellenar_lista(listaC2)
print(listaC2)
eliminar(listaC,listaC2,listaC3)
print(listaC3)