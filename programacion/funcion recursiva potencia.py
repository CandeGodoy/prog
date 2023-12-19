
def recursiva(num,po):
    if po==0:
        return 1
    return num * recursiva(num,po-1)



numero = int(input("Ingrese un numero: "))
potencia= int(input("Ingrese un numero: "))
print(recursiva(numero,potencia))