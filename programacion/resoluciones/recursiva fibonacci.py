def recursiva(numero):
    if numero==0 or numero==1:
        return numero
    else:
        return recursiva(numero-1)+recursiva(numero-2)
    
    
num= int(input(""))

print(recursiva(num))