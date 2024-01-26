def recursiva(con):
    if con==set():
        return 0
    else:
        valor = con.pop()
        return 1 + recursiva(con)
    

conjunto = {1,2,4,"caca",1}

print(recursiva(conjunto))

