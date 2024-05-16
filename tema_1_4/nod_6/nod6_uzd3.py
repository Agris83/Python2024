saraksts=[]
rev_sar=[]

teksts=input("Ievadiet tekstu: ")

saraksts=teksts.lower().split()

for el in saraksts:
    rev_sar.append(el[::-1])

teksts=""
for el in rev_sar:
    if len(teksts)>0:
        teksts+=" "        
    teksts+=el
    

print(rev_sar)
print(teksts.capitalize())

