import random

def crear_matriz(n,matriz):
    for f in range(n):
        matriz.append([])
        for c in range(3):
            matriz[f].append(0)
            

def distribuir(jug,matrizNaipes):
    
    listaCartas = [str(i)+" de "+palo for i in range(1,12) for palo in["Espada","Oro","Basto","Copas"] if i!=8 or i!=9]
    for fila in range(jug):
        for colum in range(3):
            azar = random.choice(listaCartas)
            matrizNaipes[fila][colum]= azar
            listaCartas.remove(azar)
    return matrizNaipes




#----------PROGRAMA PRINCIPAL
            
        
matrizCartas = []

jugadores = int(input("Ingrese el num de jugaores: "))

while jugadores<2 or jugadores>6:
    jugadores = int(input("ERROR - Ingrese el num de jugaores: "))
    
crear_matriz(jugadores,matrizCartas)
mm = distribuir(jugadores,matrizCartas)

print("\n")
print("\t\tCARTAS\n")
for num,ffila in enumerate(mm):
    print("Jugador",num+1,end=": ")
    for elemento in ffila:
        print("%15s"%elemento,end="\t")
    print()
