
def imprimir(lista1,lista2):
    print("URGENCIA\tTURNO")
    for i in range(len(lista1)):
        print(lista1[i],lista2[i])
        
    


#----------------PROGRAMA PRINCIPAL
listaP=[]
listaT=[]

numero = int(input("Ingrese num afiliado: "))

while numero!=-1:
    
    tipo = int(input("Ingrese urgencia(0) o  turno(1): "))
    if tipo == 0:
        listaP.append(numero)
    else:
        listaT.append(numero)
    numero = int(input("Ingrese num afiliado: "))
    
imprimir(listaP,listaT)