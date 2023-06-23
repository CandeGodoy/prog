def ingresa_valida(li,ls,texto):
    num=int(input(texto))
    while num<li or num>ls:
        num=int(input(texto))
    return num

def leecategoria():
    cate = input("Ingrese la categoria: ")
    return cate

def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

def minimo(lista):
    for i in range(len(lista)):
        if i==0 or lista[i]<minimo:
            minimo=lista[i]
    return minimo
#---------------PROGRAMA PRINCIPAL

categorias = ["A","B","C","D","E"]
categoriass= []
importes = [10000,12000,13000,14000,15000]
NroInterno=[]
cantC=[0]*5
año=[]
cont=0

categoria = leecategoria()

while cont<10 and categoria !="F":
    cont+=1
    categoriass.append(categoria)
    NroRegistro = ingresa_valida(10000,99999,"Ingrese el numero interno de registro: ")
    NroInterno.append(NroRegistro)
    añoF = ingresa_valida(1975,1990,"Ingrese el año de fabricacion: ")
    año.append(añoF)
    
    if cont<10:
        categoria = leecategoria()
        
pago = int(input("Ingrese el numero interno de registro para realizar el pago: "))

while pago!=0:
    buscar = busqueda(NroInterno,pago)
    if buscar !=-1:
        busque = categoriass[buscar]
        cate = busqueda(categorias,busque)
        cantC[cate]+=1
    else:
        print("PAGO RECHAZADO")
    pago = int(input("Ingrese el numero interno de registro para realizar el pago: "))
        
print("\n\tRECAUDACION POR CATEGORIA")
print("\tCATEGORIA\tIMPORTE")
for i in range(len(categorias)):
    print("\t",categorias[i],"\t\t",importes[i]*cantC[i])
    
añoM = minimo(año)
print("El año de fabricacion mas antiguo es: ", añoM)
