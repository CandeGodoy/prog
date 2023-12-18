#Ejercicio 3
"""Godoy, María Candela - Zeisel, Nina - Casais, Leila - Florindo, Maria Victoria - Nazar, Zahira"""

def calcular_gastos(valor,viajes):
    total=0
    if(viajes<=20):
        total=viajes*valor
    elif(viajes<=30):
        total = (valor*20)+(viajes-20)*(valor*0.8)
    elif(viajes<=40):
        total = (valor*20)+(valor*0.8*10)+(viajes-30)*(valor*0.7)
    else:
        total = (valor*20)+(valor*0.8*10)+(valor*0.7*10)+(viajes-40)*(valor*0.6)
    return total


#-----------------PROGRAMA PRINCIPIAL

valorPasaje = int(input("Ingrese el valor del pasaje: "))

cantViajes = int(input("Ingrese la cantidad de viajes realizados: "))

print(calcular_gastos(valorPasaje,cantViajes))