
conjunto = set(range(10))

print(conjunto)

while True:
    try:
        numero = int(input("Ingrese numero a eliminar: "))
        
        if numero ==-1:
            break
        conjunto.remove(numero)
        print(conjunto)

        
    except KeyError as mensaje:
        print("Numero inexistente",mensaje)
    except ValueError as mensaje:
        print("Solo ingresar numeros",mensaje)