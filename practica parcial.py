"""
Un consultorio odontológico que atiene únicamente en forma PARTICULAR trabaja con tres tipos de 
prácticas:
- EXTRACCIONES (CODIGO=E)
- TRATAMIENTO DE CONDUCTO (CODIGO =T)
- IMPLANTES (CODIGO=I)
- CONSULTA DE CONTROL (CODIGO =C)
Cada practica tiene un costo que el paciente abona:
EXTRACCIONES $10000, TRATAMIENTO DE CONDUCTO $15000, IMPLANTES $90000, CONSULTA DE 
CONTROL $5000
Cada vez que un paciente se atiende se ingresa: 
• DNI (Valor entre 10000000 y 99999999) - UTILIZAR FUNCION validarEnRango QUE VALIDE EL INGRESO 
DE ESTE DATO
• Código de practica - UTILIZAR FUNCION ingresaCodigo PARA EL INGRESO DE ESTE DATO.
• Edad del paciente (únicamente mayores a 21 años)
El registro de las atenciones finaliza con un DNI de paciente igual a -1.
Si algún paciente refiere una practica que no se ofrece indicar un error, se deberán guardar e informar al 
finalizar el listado de practicas rechazadas y a que DNI las solicito.
a. Informar el total recaudado por practica y el total general.
b. Informar la cantidad de prácticas de cada tipo se atendieron
c. Informar la edad del paciente más joven que se realizaron implantes (puede haber varios)
"""


def validarEnRango(li,ls,cf,texto):
    num=int(input(texto))
    while (num<li or num>ls)and num!=cf:
        num=int(input(texto))
    return num

def ingresaCodigo():
    codigo=input("Ingrese el codigo: ")
    return codigo

def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos
    
#-----------------------PROGRAMA PRINCIPAL
codigos = ["E","T","I","C"]
importes = [10000,15000,90000,5000]
pracR =[]
dniR = []
cantP = [0]*4
band=0


dni = validarEnRango(10000000,99999999,-1,"Ingrese su DNI: ")

while dni!=-1:
    edad = int(input("Ingrese su edad: "))
    
    if edad>21:
        codigo = ingresaCodigo()
        posicion = busqueda(codigos,codigo)
        
        if posicion!=-1:
            cantP[posicion]+=1
            if codigo=="I":
                if band==0 or edad<minimo:
                    minimo=edad
                    band=1
        
        else:
            dniR.append(dni)
            pracR.append(codigo)
    else:
        print("No se atienden a menores de 21")
        dni=-1
    dni = validarEnRango(10000000,99999999,-1,"Ingrese su DNI: ")
suma=0
print("\n\tRECAUDACION POR PRACTICAS")
print("\tPRACTICA\tRECAUDACION\tCANTIDAD")
for i in range(len(cantP)):
    suma+=cantP[i]*importes[i]
    print("\t",codigos[i],"\t\t",cantP[i]*importes[i],"\t\t",cantP[i])
print("TOTAL RECAUDADO",suma)

print("\n\tPRACTICAS RECHAZADAS")
print("\tDNI\tCODIGO")
for i in range(len(dniR)):
    print("\t",dniR[i],"\t\t",pracR[i]) 
print("La edad minima que se realizo implantes es: ",minimo)
