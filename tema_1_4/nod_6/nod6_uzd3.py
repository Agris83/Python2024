saraksts=[]
rev_sar=[]

teksts=input("Ievadiet tekstu: ")

saraksts=teksts.split()

for el in saraksts:
    rev_sar.append(el[::-1])

print(rev_sar)

