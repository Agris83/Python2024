#pitonā masīvus sauc par sarakstiem
# - order
# - mutable
# - dublikāti
# - dažādi tipi
# - dinamisks

# piton saraksts ir lēnaks nekā klasiskais masīvs

empty_list=[] # aizpilda vēlāk
prices=[1.99, 2.99, 3.50, 4.99]

print(empty_list)
print(prices)

print(f"garums {len(prices)}")

print(f"pirmā cena {prices[0]}")
print(f"pēdējā cena {prices[-1]}")

# rēķināt vidējo
total=sum(prices)

print(f"summ: {total}")

averige=total/len(prices)
print(f"vidējā cena: {averige}")

import statistics
median=statistics.median(prices)
print(f"mediāna: {median}")

beers = ["Aldaris", "Cēsu", "Piebalga"]
print(f"Ali: {beers}")

beers.append("Tērvete")
print(f"visi ali: {beers}")

beers.insert(1, "Bauska") # pielikām kā otro elementu
print(f"Papildinati ali: {beers}")

beers=beers + ["Valmiermuiža"]
print(f"vēl ali: {beers}")

first3=beers[:3] # idejiski strādā tāpat, kā ar string
last3=beers[-3:]

print(f"pirmie triis {first3} un pēdējie triis: {last3}")

beers=first3 + ["labietis"] + last3
print(f"atkal ali: {beers}")

# apgriezt listu otrādi
beers_reverse=beers[::-1]

print(f"apgrieztie ali: {beers_reverse}")

beers.reverse()
print(f"apgrieztie ali: {beers}")
beers.reverse()

# kopēt
beers_alias=beers # tas ir alias

beers_copy = beers.copy()

beers.remove("Aldaris")
print(beers)
print(beers_alias)
print(beers_copy)
print(beers_reverse)

# slicing vienmēr taisa jaunu sarakstu, pilnu kopiju
beers_copy=beers[:] # arī šādi strādātu pilna kopija


#beers == beers_copy - salidzina pēc satura un secības, pilīgi identiski

beers.append("Zoltners")
print(beers)

# check existence

print(f"Vai ir Zoltners {'Zoltners' in beers}")

print(f"meklē indeksu: {beers.index('Zoltners')}")

# nav FIND metodes Listam, bet stringam tomēr ir
beers.append('labietis')
print(f"Cik ir labieši {beers.count('labietis')}")

beers_sorted = sorted(beers)
print(f"Sakārtotie ali: {beers_sorted}")
print(f"Sakārtotie ali: {beers}")

beers.sort() # sakārto orģinālus

beers.append("Ābols")
beers.sort()

print(f"latviešu ali nesakārtojas {beers}")

beers.sort(key=len)
print(f"sakārto pēc garuma: {beers}")

prices.sort(reverse=True) # arī šādi var
print(f"apgrieztās cenas: {prices}")

beers.append(["Carlsons", "Dundulis", "Užavas"])
# beers.extend(["Carlsons", "Dundulis", "Užavas"])
print(beers)

print(f"Užavas {beers[-1][-1]}")

last_beers = beers.pop() # izmet un atgriež pēdējo elementu
print(last_beers)
print(beers)

beers.extend(["super Bock", "Duff Beer", "Užavas"])
print(beers)

beers.clear # izmet visu ārā

beers=beers_copy.copy()

# print(f"pēdējie 5000 beers {beers[-5000:]}") # slicingam nav indeksācijas kļūdu, atgeizt var vienmēr visu


for beer in beers:
    print(beer)

for i, beer in enumerate(beers, start =1):
    print(f"Beer No.{i}. {beer}")

beers.append("Lowenbrau")

print(beers)

beers_with_l = []
for beer in beers:
    if beer.upper().startswith("L"):
        beers_with_l.append(beer)
print(beers_with_l)







