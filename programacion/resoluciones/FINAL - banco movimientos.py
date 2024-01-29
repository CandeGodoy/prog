
def contar_saldo(lista):
    if len(lista)==0:
        return 0
    else:
        return float(lista[0]) + contar_saldo(lista[1:])

try:
    arch = open("movimientos.txt","rt")
    saldos = open("clientes.txt","wt")
    deudores = []
    
    for linea in arch:
        linea = linea.rstrip("\n")
        cliente = linea.split(";")
        
        final = contar_saldo(cliente[2:])
        
        saldos.write(cliente[0]+";"+cliente[1]+";"+f"{final:.2f}"+"\n")
        
        if final<0:
            deudores.append([cliente[0]]+[cliente[1]]+[final])
            
    deudores.sort(key=lambda x:x[2])
    
    for d in deudores:
        for dd in d:
            print(f"{dd:^20}",end="")
        print()
        
    
except FileNotFoundError as mensaje:
    print("No se puede leer el archivo: ",mensaje)
except OSError as mensaje:
    print("ERROR: ",mensaje)
finally:
    try:
        arch.close()
        saldos.close()
    except NameError:
        pass