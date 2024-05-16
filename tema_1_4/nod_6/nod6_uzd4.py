
sk=2
i=2
skaitli=[]
cik=int(input("Ievadiet pirmskaitļu skaitu: "))


while len(skaitli)<cik:
    pirm_sk=True
    i=2

    while i<=int(sk**0.5):
        if sk%i == 0:
            pirm_sk=False
            break
        i+=1

    if pirm_sk==True:
        skaitli.append(sk)

    sk+=1

print(skaitli)
