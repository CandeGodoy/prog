# Ejercicio 12 - TP 2 - Programacion 1
"""Godoy, María Candela - Zeisel, Nina - Casais, Leila - Florindo, Maria Victoria - Nazar, Zahira"""

def mostrar_registros(lista1,lista2):
    print("\n\tRegistros")
    print()
    print("\tSocios\tVisitas")
    for i in range (len(lista1)):
        print("\t",lista1[i],"\t",lista2[i])

    


#------------PROGRAMA PRINCIPAL

socios=[]
visitas=[]



num = int(input("Ingrese numero de socio: "))
while num!=0:
    opcion = int(input("Ingrese 1 si desea registrar socio, ingrese 2 para eliminar sus registros: "))
        
    if(opcion==1):
        if num not in socios:
            socios.append(num)
            pos = socios.index(num)
            visitas.insert(pos,1)
            
            print("Este socio tiene", visitas[pos] ,"ingresos")
        else:
            pos=socios.index(num)
            visitas[pos] += 1
            
            print("Este socio tiene", visitas[pos] ,"ingresos")
    else:
        socios.remove(num)
        pos = socios.index(num)
        visitas[pos].remove(num)
            
    num = int(input("Ingrese numero de socio: "))
mostrar_registros(socios,visitas)