def verificar(mail):
    
    valor = True
    
    dominio = mail.find("@")
        
    usuario = mail[:dominio].isalpha()
        
    if usuario == False:
        print("Solo se permiten caracteres alfanumericos")
        valor = False
        
    repe = mail.count("@")
    
    if repe>1:
        print("Solo se permite un @")
        valor = False
        
        
    return valor










#------------------PROGRAMA PRINCIPAÑ
        
listaCorrectos = []
listaIncorrectos = []

mal = input("Ingrese un mail")

while len(mal)!=0:
    resul = verificar(mal)
    if resul:
        listaCorrectos.append(mal)
    else:
        listaIncorrectos.append(mal)
    mal = input("Ingrese un mail")

print()