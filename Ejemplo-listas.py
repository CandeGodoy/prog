'''
Cargar los legajos,apellido y nota promedio de los alumnos
de un curso.

Luego de finalizar la carga sin legajos duplicados:

1)Mostrar ambos con el formato:
Legajo - Apellido - Nota
XXXX     AAAAAAAA   XX

2) Informar el legajo del alumno que saco la nota minima
(lo asumimos unico)
3) Informar el o los legajos con nota maxima
4) Informar la nota promedio de los alumnos
5) Emitir un listado de legajos de aquellos alumnos cuya
nota es menor a la nota promedio
'''

def ingresaValidaRango (li,ls,texto):
    valor= int(input(texto))
    while valor<li or valor>ls:
        valor =  int(input(texto))
    return valor

def ingresaValidaRangoNro(li,ls,cf,texto):
    valor= int(input(texto))
    while (valor<li or valor>ls) and valor != cf:
        valor =  int(input(texto))
    return valor

def busqueda(lista,valorBuscado):
    pos = -1
    i = 0
    
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

def carga(l1,l2,l3):
    
    auxLegajo = ingresaValidaRangoNro(1000,9999,-1,"Ingrese un legajo: ")
    
    while auxLegajo !=-1:
        
        posicion=busqueda(l1,auxLegajo)
        if posicion==-1:
            auxApellido=input("Ingrese un apellido: ")
            auxNota=ingresaValidaRango(0,10,"Ingrese un nota: ")
            
            l1.append(auxLegajo)
            l2.append(auxApellido)
            l3.append(auxNota)
        
        else:
            print("Error - Legajo duplicado!")
        
        auxLegajo = ingresaValidaRangoNro(1000,9999,-1,"Ingrese un legajo: ")
 
def listado(l1,l2,l3):
    
    print("\n\tLISTADO DE ALUMNOS")
    print("  LEGAJO\tAPELLIDO\tNOTA")
    print("---------------------------------------")
    for i in range(len(l1)):
        print("",l1[i],"\t\t",l2[i],"\t\t",l3[i])
        
def min(l1,l2):
    for i in range (len(l1)):
        if i == 0 or l1[i]<minimo:
            minimo = l1[i]
            legajomin = l2[i]
    print("La nota minima es",minimo,"y su legajo es",legajomin)
    
def max(l1,l2):
    for i in range (len(l1)):
        if i == 0 or l1[i] > maximo:
            maximo = l1[i]
    print ("La nota maxima es",maximo)
    for i in range(len(l1)):
        if maximo == l1[i]:
            print ("Legajo con nota maxima:",l2[i])

def suma (l1):
    suma = 0
    for i in range (len(l1)):
        suma += l1[i]
    print(suma)
    
def prom (l1):
    sumaNota = suma(l1)
    promedio = sumaNota/(len(l1))
    print (promedio)
                   
        
#--------------PROGRAMA PRINCIPAL
legajos = []
apellidos = []
notas = []

carga(legajos,apellidos,notas)

print(legajos)
print(apellidos)
print(notas)

listado(legajos,apellidos,notas)

min(notas,legajos)
max(notas,legajos)
suma(notas)
prom(notas)
