import random

def recursiva(listaR,maxi=-1):
    if len(listaR)==0:
        return maxi 
    else:
        if listaR[0]%2==0 and(maxi==-1 or listaR[0]>maxi):
            maxi=listaR[0]
    return recursiva(listaR[1:],maxi)






lista = [random.randint(1,10) for x in range(random.randint(1,5))]

print(recursiva(lista))

