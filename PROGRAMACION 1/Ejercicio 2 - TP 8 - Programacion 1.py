def crearFecha(cad):
    meses = {
        1:"Enero",
        2:"Febrero",
        3:"Marzo",
        4:"Abril",
        5:"Mayo",
        6:"Junio",
        7:"Julio",
        8:"Agosto",
        9:"Septiembre",
        10:"Octubre",
        11:"Noviembre",
        12:"Diciembre"
        }
    messs = int(cad[1])
    return cad[0]+" de "+meses[messs]+" de "+ f"2{cad[2]:0>3}"
    
    
    
    
#------------
    
fecha =()    
    
dia = input("Ingrese el dia: ")
fecha = fecha + (dia,)
mes = input("Ingrese el mes: ")
fecha = fecha + (mes,)
año = input("Ingrese el año: ")
fecha=fecha+(año,)

print(crearFecha(fecha))