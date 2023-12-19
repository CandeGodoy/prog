import random
def venta(dia,mes,año,canti):
    AAAAV = random.randint(año,2023)
    if dia != 31:
        DDV = random.randint(dia+1,31)
    else:
        DDV = 31
    MMV = random.randint(mes,12)
    NNNV = random.randint(1,canti)
    return AAAAV,DDV,MMV,NNNV

try:
    arch = open("mercaderia.txt","wt")
    cant = random.randint(50,200)
    
    
    for i in range(cant):
        DD = random.randint(1,31)
        MM = random.randint(1,12)
        AAAA = random.randint(2002,2023)
        DDD = random.choice(["TIJERA ESCOLAR PLAST","RESMA PAPEL OBRA","LAPICERA AZUL BIC","HOJAS EXITO","LAPICERA COLOR"])
        NNN = random.randint(1,999)
        PPP = random.randint(1,999)
        PP = random.randint(1,99)
        arch.write(f"{DD:0>2}"+" "+f"{MM:0>2}"+" "+str(AAAA)+" "+f"{DDD:<20}"+" "+f"{NNN:0>3}"+" "+f"{PPP:0>3}.{PP:0>2}"+"\n")
        
        añoV,diaV,mesV,cantV=venta(DD,MM,AAAA,NNN)
        arch.write(f"{diaV:0>2}"+" "+f"{mesV:0>2}"+" "+str(añoV)+" "+f"{cantV:0>3}"+" "+f"{DDD:<20}"+" "+f"{PPP:0>3}.{PP:0>2}"+"\n")


except FileNotFoundError as mensaje:
    print("Archivo no encontrado: ",mensaje)
except OSError as mensaje:
    print("No se pudo grabar el archivo: ",mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass