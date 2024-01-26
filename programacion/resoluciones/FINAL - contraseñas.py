"""Contraseñas! En general las contraseñas a crear deben cumplir reglas por seguridad para que sean válidas.
Desarrolle un programa que ingrese contraseñas hasta ingresar una contraseña vacía. A medida que se ingresan verifique e informe si cumple con las reglas:
a. Debe comenzar con un carácter alfabético.
b. Debe contener al menos dos letras mayúscula. Contar la cantidad de letras mayúscula de una cadena mediante una función recursiva.
Resolver utilizando exclusivamente manejo de excepciones y estructura While-True,
creando una nueva excepción o utilizando una existente (ValueError) cuando no cumpla alguno de las dos reglas, mostrar mensaje aclaratorio correspondiente en cada caso."""
def contar(palabra):
    if len(palabra)==0:
        return 0
    elif palabra[0].isupper():
        return 1+contar(palabra[1:])
    return contar(palabra[1:])

#------------------------------------------
while True:
    try:
        contraseña = input("Ingrese la contraseña: ")        
        
        while contraseña!="":
            assert contraseña[0].isalpha(),"DEBE COMENZAR CON UN CARACTER"
            mayus = contar(contraseña)
            print("La contraseña",contraseña,"tiene",mayus,"mayusculas")
            contraseña = input("Ingrese la contraseña: ")
            
            
        break
    except AssertionError as mensaje:
        print(mensaje)