"""El segundo te informaba que habian dos aviones F y J. El avión F tenía 180 filas y asientos de la A a la F.El avion J tenia +300 filas y asientos de la A a la J.
A partir de esa información te daba un csv donde los punto y coma dividian nombre de pasajero, fila en numeros y asiento en letras (Juan Perez;3;A).
Si la linea solamente especificaba el nombre del pasajero (Juan Perez) era porque este habia pagado menos que los que si tenian asignado un asiento y el asiento se le iba a asignar al azar teniendo
en cuenta los que ya estaban ocupados por los que habian pagado más.
El programa debía informar por cada pasajero que asiento y fila le habia tocado y también informar cuales eran las filas y asientos libres en los aviones. No habia que informar que avion."""
import random

#------------------------------------------------------
try:
    arch = open("informacion.txt","rt",encoding="utf-8")
    

    numeros = [[i]+[k] for k in ["A","B","C","D","E","F","G","H","I","J"] for i in range(1,10+1) ]

    print("\tPASAJERO\t    FILA\t\tASIENTO")
    ocupados =[]
    for linea in arch:
        linea = linea.rstrip("\n")
        pasajero = linea.split(";")
        
        if len(pasajero)!=1:
            for l in pasajero:
                print(f"{l:^20}",end="")
            ocupados.append(pasajero[1:])
            if pasajero[1:] in numeros:
                numeros.remove(pasajero[1:])
            print()
    arch.seek(0)
    
    libres = [["LIBRE"]+e for e in numeros]
    
    for linea2 in arch:
        linea2 = linea2.rstrip("\n")
        pasajero2 = linea2.split(";")

        if len(pasajero2)==1:
            asiento = random.choice(numeros)
            numeros.remove(asiento)
            pasajero2= pasajero2+asiento
            for ll in pasajero2:
                print(f"{ll:^20}",end="")
            print()
    print("\n")        
    print("\t\t\tASIENTOS LIBRES")
    print("\t        \t    FILA\t\tASIENTO")
    for dd in libres:
        for ddd in dd:
            print(f"{ddd:^20}",end="")
        print()
    
            
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass