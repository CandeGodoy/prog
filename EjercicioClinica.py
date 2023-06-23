"""
Una clínica necesita un programa para atender a sus pacientes.

Cada paciente que ingresa se anuncia en la recepción indicando su
número de afiliado (número entero de 4 dígitos) y
además indica si viene por una urgencia (ingresando un 0) o con 
turno (ingresando un 1).
Para finalizar se ingresa -1 como número de socio.
Luego se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de 
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue 
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta 
que se ingrese -1 como número de afiliado.
"""
def ingresaValidaRangoNro(li,ls,cf,texto):
    valor=int(input(texto))
    while (valor<li or valor>ls) and valor !=cf:
        valor=int(input(texto))
    return valor    

def listarSocios(l1,l2,condicion):
    #condicion=0 => socios x urgencia
    #condicion=1 => socios x turno
    
    if condicion ==0:
        print("SOCIOS ATENDIDOS POR URGENCIA")
    else:
        print("SOCIOS ATENDIDOS POR TURNO")
       
    for i in range(len(l1)):
        if l2[i]==condicion:
            print(l1[i])
        
        
def busqueda(lista,valorBuscado):
    pos=-1
    i=0    
    while pos==-1 and i<len(lista):
        if valorBuscado==lista[i]:
            pos=i
        i+=1
    return pos       


#aqui comienza el programa principal
socios=[]
tAtencion=[]

#carga inicial de los datos
auxSocio=ingresaValidaRangoNro(1000,9999,-1,"Ingrese un numero de socio ")
while auxSocio !=-1:
    
    auxTipoAtencion=int(input("Ingrese 0=Urgencia 1=Turno "))
    while auxTipoAtencion!=0 and auxTipoAtencion !=1:
        auxTipoAtencion=int(input("Ingrese 0=Urgencia 1=Turno "))
    
    #vamos a guardar los datos en la lista
    socios.append(auxSocio)
    tAtencion.append(auxTipoAtencion)
    
    auxSocio=ingresaValidaRangoNro(1000,9999,-1,"Ingrese un numero de socio ")

print(socios)
print(tAtencion)
    
listarSocios(socios,tAtencion,0)
listarSocios(socios,tAtencion,1)

print("\n\nCOMENZAMOS LA CONSULTA DE SOCIOS....")

auxSocio=ingresaValidaRangoNro(1000,9999,-1,"Ingrese un numero de socio ")
while auxSocio !=-1:
    contTURNOS=0
    contURGENCIA=0
    
    posicion =busqueda(socios,auxSocio)
    
    if posicion==-1:
        print("SOCIO SIN ATENCION!!!")
    else:
        for i in range(len(socios)):
            if socios[i]==auxSocio:
                if tAtencion[i]==1:
                    contTURNOS+=1
                else:
                    contURGENCIA+=1
        print("CANTIDAD ATENCION X URGENCIA ->", contURGENCIA)
        print("CANTIDAD ATENCION X TURNO ->", contTURNOS)
                   
    auxSocio=ingresaValidaRangoNro(1000,9999,-1,"Ingrese un numero de socio ")
      
            
            
            
            
    
    
    
    
    
        





