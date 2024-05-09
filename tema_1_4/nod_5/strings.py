
food = "pica"
print(food)

drink="kaffija"
print(f"man garši {drink}")

ttt="kaut kāds 'teksts'"
print(ttt)

teksts='es saku, \'gribu ēst\''
print(teksts)

teksts="divas \nrindas"
print(teksts)

gara_rinda="""kaut kas
vēl kaut kaut kas
    arī vēl kaut kas"""

print(gara_rinda)

name="Agris"
age=42
f_str=f"mani sauc {name} un man ir {age} gadi"
print(f_str)

r=10
PI=3.1415926

area=PI * r ** 2
area_string = f"radiuss {r} ir {area:.2f}"
print(area_string)

area_string = f"radiuss {r:05} ir {area:.3f}"
print(area_string)

food_length = len(food)
print(f"edienam {food} ir garums {food_length}")

pirmais_burts = food[0]
print(pirmais_burts)

ped_b= food[len(food)-1]
print(ped_b)

ped_b=food[-1] # pēdējais burts, pitonā ir negatīva indeksācija
print(ped_b)

try:
    arpus_kartas=food[10]
except IndexError as e:
    print(f"Indeksa errors {e}")

# 3 pirnie simboli
pirmie_tris=food[:3]
print(pirmie_tris)

# pēdējie 3
ped_3=food[-3:]
print(ped_3)

food="kartupelis"
vidus=food[3:6]
print(vidus)

vidus=food[3:-3]
print(vidus)

k_otrais=food[::2]
print(k_otrais)

#no 4 lidz ...
ttt=food[3:-3:3]
print(ttt)

# teksta apgriešana
rev_food=food[::-1]
print(rev_food)

rev_food=food[::-2]
print(rev_food)

# eksistences pārbaude
if "a" in food:
    print(f"vārdā {food} ir a!")
else:
    print(f"vārdā {food} nav a!")


