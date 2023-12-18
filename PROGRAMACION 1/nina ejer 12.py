# Ejercicio 12 - TP2 - Programacion 1
def mostrar_registros(lista1,lista2):
    print("\n\tRegistros")
    print()
    print("\tSocios\tVisitas")
    for i in range (len(lista1)):
        print("\t",lista1[i],"\t",lista2[i])
    
def eliminar_ingresos(numero,lista1,lista2):
    pos = lista1.index(numero)
    lista1.remove(numero)
    lista2.pop(pos)
    
    

#---- PROGRAMA PRINCIPAL
socios =[]
visitas =[]


nSocio = int(input("Ingrese su numero de socio:"))

while nSocio != 0:
    
    opcion = int(input("Ingrese 1 si desea registrar socio, ingrese 2 para eliminar sus registros: "))
    
    if opcion == 1:
        if nSocio in socios:
            pos = socios.index(nSocio)
            visitas[pos] += 1
            
            print("Este socio tiene", visitas[pos] ,"ingresos")
            
        else:
            socios.append(nSocio)
            pos = socios.index(nSocio)
            visitas.insert(pos,1)
            
            print("Este socio tiene" ,visitas[pos], "ingresos")


    elif opcion == 2:
        if nSocio in socios:
            mostrar_registros(socios,visitas)
            eliminar_ingresos(nSocio,socios,visitas)
            mostrar_registros(socios,visitas)
            
        else:
            print("ERROR - Este numero de socio no se encuentra en el sistema")
            
    nSocio = int(input("Ingrese su numero de socio:"))