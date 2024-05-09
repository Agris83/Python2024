import math

i=2
pirm_sk=True

sk=int(input("ievadiet skaitli: "))

while i<= int(math.sqrt(sk)):
    if sk%i == 0:
        pirm_sk=False

    i+=1

if pirm_sk==True:
    print(f"Ievadītais skaitlis {sk} ir pirmskaitlis!")
else:
    print(f"Ievadītais skaitlis {sk} NAV pirmskaitlis!")