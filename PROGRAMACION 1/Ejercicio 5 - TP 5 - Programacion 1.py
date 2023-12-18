import math 

try:
    numero = input("Ingrese un numero: ")
    raiz = math.sqrt(float(numero))
    print(f"La raíz de {numero} es {raiz}")
except ValueError:
        print(f"Error - No se puede calcular la raíz de {numero}")
    