año1 = int(input("Ingrese un año: "))
año2 = int(input("Ingrese otro año: "))

años = [x for x in range(año1,año2+1) if x%4==0 and x%100!=0 or x%400==0]

print(años)