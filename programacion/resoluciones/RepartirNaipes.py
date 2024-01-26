import random

def distribuircartas(jugadores):
    # Creamos una lista por comprensión con todas las cartas
    listacartas = [str(n)+" de "+palo for palo in ["Oros", "Copas", "Bastos", "Espadas"] for n in range(1,13) if n not in [8, 9]]
    # y elegimos todas las cartas que serán necesarias. Luego las cargaremos en la matriz
    mano = []
    for i in range(jugadores*3):   # Tres cartas por jugador
        # elegimos un carta al azar
        carta = random.choice(listacartas)
        # La agregamos a la lista de cartas seleccionadas
        mano.append(carta)
        # Y la eliminamos del mazo para no repetirla
        listacartas.remove(carta)
    # Ahora armamos la matriz trozando la lista
    matriz = []
    for i in range(jugadores):
        matriz.append(mano[i*3:i*3+3])
    return matriz
    
# Programa principal
jug = int(input("Cantidad de jugadores (2 a 6)? "))
while jug<2 or jug>6:
    jug = int(input("Cantidad de jugadores (2 a 6)? "))
print()
cartas = distribuircartas(jug)
for i,jugador in enumerate(cartas):
    print("Jugador", i+1, end= ":  ")
    for carta in jugador:
        print("%15s" %carta, end="")
    print()