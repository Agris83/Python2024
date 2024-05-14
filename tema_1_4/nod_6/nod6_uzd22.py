
saraksts=[]

a=int(input("Ievadiet sākuma skaitli: "))
b=int(input("Ievadiet beigu skaitli: "))

for i in range(a,b+1):
    saraksts.append(i**3)
    print(i, "kubā", saraksts[-1])

print(f"Visi kubi: {saraksts}")
