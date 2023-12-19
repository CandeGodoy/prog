def esnumerodefischer(n):
    # Construimos una lista por comprensión con los divisores del número, incluyendo al propio número
    divisores = [d for d in range(1, n+1) if n%d==0]
    # Ahora que tenemos la lista de divisores, calculamos su producto
    producto = 1
    for i in divisores:
        producto = producto * i
    # Verificamos si el producto de los divisores coincide con el cubo del número
    if producto == n**3:
        return True
    else:
        return False

# Programa principal
n = int(input("Ingrese un número entero: "))
print("Números de Fischer entre 1 y", n)
for i in range(1,n+1):
    if esnumerodefischer(i):
        print(i, end=" ")
print()