
def triangulo(lista):
    copia = lista.copy()
    def recursiva(copia):
        if len(copia)==1:
            return []
        else:
            return [copia[0]+copia[1]] + recursiva(copia[1:])
            
    sumatoria = recursiva(copia)
    
    return [lista] + triangulo(sumatoria)
    

listak=[]
listaN = [1,2,3]
print(triangulo(listaN))