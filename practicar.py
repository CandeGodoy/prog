'''
Cargar los legajos,apellido y nota promedio de los alumnos
de un curso.

Luego de finalizar la carga sin legajos duplicados:

1)Mostrar ambos con el formato:
Legajo - Apellido - Nota
 XXXX	 AAAAAAAA   XX
 
2) Informar el legajo del alumno que saco la nota minima
(lo asumimos unico)

3) Informar el o los legajos con nota maxima

4) Informar la nota promedio de los alumnos

5) Emitir un listado de legajos de aquellos alumnos cuya
nota es menor a la nota promedio
'''
def ingresaValidaRango(li,ls,texto):
    num = int(input(texto))
    while num<li or num>ls:
        num = int(input(texto))
    return num

def ingresaValidaRangoNro(li,ls,cf,texto):
    num = int(input(texto))
    while (num<li or num>ls) and num!=cf:
        num = int(input(texto))
    return num

def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

def min(lista,lista2):
    for i in range(len(lista)):
        if i==0 or lista[i]<minimo:
            minimo=lista[i]
            legajoMin=lista2[i]
    print("La nota minima es:",minimo,"correspondiente al legajo:",legajoMin)

def max(lista,lista2):
    for i in range(len(lista)):
        if i==0 or lista[i]>maximo:
            maximo=lista[i]
    print("La nota maxima es: ",maximo)
    for i in range(len(lista2)):
        if maximo == lista[i]:
            print("Los legajos con nota maxima son: ",lista2[i])

def suma(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma

def prom(lista):
    total = suma(lista)
    return total/len(lista)

def notaMenorProm(lista,lista2):
    promedio = prom(lista)
    for i in range(len(lista)):
        if lista[i]<promedio:
            print("Los legajos menores al promedio son: ",lista2[i])
            
#------------------------PROGRAMA PRINCIPAL

legajos=[]
apellidos=[]
notas=[]

legajo = ingresaValidaRangoNro(1000,9999,-1,"Ingrese nro de legajo: ")

while legajo!=-1:
    buscar = busqueda(legajos,legajo)
    if buscar==-1:
        legajos.append(legajo)
        apellido = input("Ingrese el apellido: ")
        apellidos.append(apellido)
        nota = ingresaValidaRango(1,10,"Ingrese la nota: ")
        notas.append(nota)
    else:
        print("ERROR - legajo duplicado")
        
    legajo = ingresaValidaRangoNro(1000,9999,-1,"Ingrese nro de legajo: ")

print("\n\tLISTADO DE ALUMNOS")
print("  LEGAJO\tAPELLIDO\tNOTA")
for i in range(len(legajos)):
    print("\t",legajos[i],"\t",apellidos[i],"\t\t",notas[i])
    
minimo = min(notas,legajos)
max(notas,legajos)

print("El promedio es: ", prom(notas))

notaMenorProm(notas,legajos)