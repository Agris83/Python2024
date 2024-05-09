import math

i=2
pirm_sk=True

sk=int(input("ievadiet skaitli: "))

# while i<int(sk**0.5) # šādi var izmantot bez math
while i<= int(math.sqrt(sk)): # šādi dara math bibliotēku
    if sk%i == 0:
        pirm_sk=False
        break

    i+=1

if pirm_sk==True:
    print(f"Ievadītais skaitlis {sk} ir pirmskaitlis!")
else:
    print(f"Ievadītais skaitlis {sk} NAV pirmskaitlis!")

