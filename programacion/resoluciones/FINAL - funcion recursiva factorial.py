def recursiva(num):
    if num==0:
        return 1
    return num * recursiva(num-1)
    

#---------------------
while True:
    try:
        numero = int(input("Ingrese un numero"))
    
        assert numero>=0 and numero<=10, "ERROR - numero fuera de rango"
        print(recursiva(numero))
        break
    except AssertionError as mensaje:
        print(mensaje)
