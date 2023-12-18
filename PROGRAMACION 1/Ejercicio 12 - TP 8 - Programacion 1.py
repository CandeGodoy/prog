def aumentar():
    pass


#-------------------

dic={}

nombre = input("Ingrese el nombre del libro: ")


while nombre!="":
    precio = int(input("Ingrese su precio: "))
    dic[nombre] = precio
    nombre = input("Ingrese el nombre del libro: ")
    
    
for clave, valor in dic.items():
    dic[clave] = valor+((valor*15)/100)

costoso = max(dic.keys())
    
print(dic)

print("El Item mas costoso es",costoso,", el cual tiene un precio de ",dic[costoso])