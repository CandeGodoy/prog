

año1=int(input("Inmgrese"))
año2=int(input("Inmgrese"))

años =[x for x in range(año1,año2+1) if x%4==0 and x%100!=0]
print(años)