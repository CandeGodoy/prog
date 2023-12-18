def sumar(num1,num2):
    try:
        total = float(num1)+float(num2)
    except ValueError:
        total = -1
    return total


#-----------PROGRAMA PRINCIPAL


cadena1 = input("Ingrese un numero: ")
cadena2 = input("Ingrese un numero: ")
print(sumar(cadena1,cadena2))


