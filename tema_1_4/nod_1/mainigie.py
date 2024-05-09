# mainīgie
# nav jādefinē mainīgais
# datu tipi piesaistās dinamiski
# name = "Agris" # konstants mainīgais
name = input("Kāds ir Tavs vārds?")
print(name)
print("Sveiks",name)
print("Sveiks "+name)
print(f"Sveiks {name}") # ieteicams vieds, bet var izmantot arī iepriekšējos, jo šis būs vnkērtāk

print(f"kāds ir Tavs mīļākais ēdiens {name}?", end="") # lai nepārlektu jaunā rindā
food = input() # kaut kāds teksts
quantity = input("Cik kg?")
price = input("Cik maksā?")

quantity=int(quantity) # nomaina datu tipu
price=float(price)
total=quantity * price

total_round = round(total, 2) # izmanto noapaļošanai, kā arī lai izvairītos no float gļukiem, 7 * 0.1

print(f"{name} Tev par {food} būs jāmaksā {total}!")
print(f"{name} Tev par {food} būs jāmaksā {total_round}!")



