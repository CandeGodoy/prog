def sumar(num1,num2):
    total = float(num1)+float(num2)
    return total


#-----------PROGRAMA PRINCIPAL

try:
    cadena1 = input("Ingrese un numero: ")
    cadena2 = input("Ingrese un numero: ")
    print(sumar(cadena1,cadena2))
except ValueError:
    print("-1")
