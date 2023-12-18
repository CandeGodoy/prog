#Ejercicio 4
"""Godoy, María Candela - Zeisel, Nina - Casais, Leila - Florindo, Maria Victoria - Nazar, Zahira"""

def calcular_vuelto(a,b):
    vuelto = a - b
    if vuelto != 0:
        cambio500 = vuelto // 500
        vuelto = vuelto % 500
        cambio100 = vuelto // 100
        vuelto = vuelto % 100
        cambio50 = vuelto // 50
        vuelto = vuelto % 50
        cambio20 = vuelto // 20
        vuelto = vuelto % 20
        cambio10 = vuelto // 10
        vuelto = vuelto % 10
        cambio5 = vuelto // 5
        vuelto = vuelto % 5
        cambio1 = vuelto // 1
        
    return cambio500, cambio100, cambio50,cambio20, cambio10, cambio5, cambio1
    
# --------- PROGRAMA PRINCIPAL

recibido = int(input("Ingrese el monto de dinero que ha recibido: "))
totalCompra = int(input("Ingrese el total de la compra: "))

billete500,billete100,billete50,billete20,billete10,billete5,billete1 = calcular_vuelto(recibido,totalCompra)

print(billete500,"billetes de quinentos")
print(billete100,"billetes de cien")
print(billete50,"billetes de cincuenta")
print(billete20,"billetes de veinte")
print(billete10,"billetes de diez")
print(billete5,"billetes de cinco")
print(billete1,"billetes de uno")
