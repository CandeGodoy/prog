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
    #li=limite inferior
    #ls=limite superior
    #cf=condicion fin
    #texto= texto o mensaje al usuario
    
    valor=int(input(texto))
    while (valor<li or valor>ls) and valor !=cf:
        valor=int(input(texto))
    return valor

def busqueda(lista,valorBuscado):
    
    pos=-1
    i=0
    while i<len(lista) and pos==-1:
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

#aqui comienza el programa principal
CANTPRA=[0]*4
IMPORTES=[10000,15000,90000,5000]
PRACTICAS=['E','T','I','C']
dniR=[]
praR=[]

band=0
i=0

auxDni=validarEnRango(10000000,99999999,-1,"Ingrese un dni ")

while auxDni!=-1:
    i+=1 
    auxEdad=int(input("Ingrese una edad mayor a 21"))
    
    if auxEdad>21:
        auxPrac=input("Ingrese una practica ")
        
        
        posicion=busqueda(PRACTICAS,auxPrac)
        
        if posicion ==-1:
            dniR.append(auxDni)
            praR.append(auxPrac)
        else:
            CANTPRA[posicion]+=1
            
            if auxPrac=='I':
                if band==0 or edadMinI<auxEdad:
                    edadMinI=auxEdad
                    band=1
            
    else:
        print("No se puede atender por ser menor a 21 años!")
    
    auxDni=validarEnRango(10000000,99999999,-1,"Ingrese un dni ")
   
   
if i>0:
    """
    a. Informar el total recaudado por practica y el total general.
    """
    suma=0
    print("\n\nRECAUDACION POR PRACTICA")
    for i in range(len(PRACTICAS)):
        suma+=CANTPRA[i]*IMPORTES[i]
        print("\t",PRACTICAS[i],"\t",CANTPRA[i]*IMPORTES[i])
    print("TOTAL RECAUDADO ", suma)

    """
    b. Informar la cantidad de prácticas de cada tipo se atendieron
    """
    print("\n\nCANTIDAD DE ATENCIONES POR PRACTICA")
    for i in range(len(PRACTICAS)):    
        print("\t",PRACTICAS[i],"\t",CANTPRA[i])

    print("\n\nDNI CON PRACTICAS RECHAZADAS")
    for i in range(len(dniR)):
        print("\t",dniR[i],"\t",praR[i])
    
    print("\n\nLa edad del paciente mas joven que se hizo un implante es ",edadMinI)
else:
    print("NO SE INGRESARON DATOS!")
    
                
            
            
            
            
    
    
    
    
    
    
    
    






