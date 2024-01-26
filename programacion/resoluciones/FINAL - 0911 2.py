

numero = int(input("Ingrese un numero: "))



triangular = lambda x: True if (((int(x**0.5)+1)*int((x**0.5)+2))//2)==x else False  
print(triangular(numero))
