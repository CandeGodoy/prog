#Ejercicio 1

def capicua(cadena):
    pos_izq=0
    pos_der=len(cadena)-1
    
    while pos_der >= pos_izq:
        if not cadena[pos_izq] == cadena[pos_der]:
            valor = False
        else:
            valor= True
        pos_izq +=1
        pos_der -=1
    
    if valor == True:
        print(cadena,"es capicua")
    else:
        print(cadena,"no es capicua")
    
#-----------------PROGRAMA PRINCIPAL

cadenaCarac=input("Ingrese una palabra: ")


capicua(cadenaCarac)

print(len(cadenaCarac))