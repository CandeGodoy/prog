#FINAL PREVIO 2022 - ARCHIVOS - RECURSIVIDAD PROMEDIO
def promedio_digitos(numero, suma=0, contador=0):
    if numero == 0:
        return suma / contador if contador > 0 else 0
    else:
        digito = numero % 10
        return promedio_digitos(numero // 10, suma + digito, contador + 1)

numero = int(input("Ingrese un número entero: "))
resultado = promedio_digitos(numero)
print(f"El promedio de los dígitos de {numero} es {resultado:.2f}")