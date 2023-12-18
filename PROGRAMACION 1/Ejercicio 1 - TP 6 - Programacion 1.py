import random

try:
    arch = open("datos.txt","wt")
    
    registros = random.randint(50,200)
    
    for i in range(registros):
        
        mes = random.randint(1,12)
        if mes==6 or mes==4 or mes==11 or mes==9:
            dia = random.randint(1,30)
        elif mes==2:
            dia = random.randint(1,29)
        else:
            dia = random.randint(1,31)
            
        lluviacaida = random.randint(0,400)
        arch.write(str(dia)+";"+str(mes)+";"+str(lluviacaida)+"\n")
    
    
except FileNotFound as mensaje:
    print("No se puede abrir el archivo: ",mensaje)
except OSError as mensaje:
    print("No se puede crear el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass