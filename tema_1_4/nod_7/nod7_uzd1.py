
def add_mult(argumenti):
    argumenti.sort()
    
    rez=(argumenti[0]+argumenti[1])*argumenti[2]
    return rez

saraksts=[]

saraksts.append(int(input("ievadiet 1. argumentu: ")))
saraksts.append(int(input("ievadiet 2. argumentu: ")))
saraksts.append(int(input("ievadiet 3. argumentu: ")))

print(add_mult(saraksts))



