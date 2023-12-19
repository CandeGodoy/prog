#Lista tope lista base

def triangulo(lista):
    if len(lista) == 1:
        return [lista]
    else:
        copia = lista.copy() 
        
        def sumas(copia):
            if len(copia) == 1:
                return []
            else:
                suma = [copia[0] + copia[1]]
                copia.pop(0)
                return suma + sumas(copia)
        
        sumatoria = sumas(copia)
        return [lista] + triangulo(sumatoria)

listaoriginal = [1, 2, 3, 4, 5]
resultado = triangulo(listaoriginal)
for nivel in range(len(resultado)-1,-1,-1):
    print(resultado[nivel])