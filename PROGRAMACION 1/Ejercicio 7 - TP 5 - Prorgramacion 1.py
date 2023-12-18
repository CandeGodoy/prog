import random

def adivinar():
    numero = random.randint(1,10)
    cont = 0
    while True:
        try:
            valor=int(input("Ingrese numero"))
            if valor == numero:
                print("Acertaste en el intento:",cont)
                break
            elif valor<numero :
                print("El numero es mayor")
                cont +=1
            else:
                print("El numero es menor")
                cont +=1

        except ValueError:
            print("Ingrese numeros ")
            cont +=1
                    
        
        
adivinar()