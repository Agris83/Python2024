
def add_unique_el_to_list(elemet, my_list):
    if elemet not in my_list:
        my_list.append(elemet)
    else:
        print(f"{elemet} ir jau listā")

foods=["ābols", "banāns", "gurķis"]

add_unique_el_to_list("ābols", foods)
add_unique_el_to_list("citrons", foods)


print(foods)

def nokluseta_v(name="Agris"):
    print(f"{name}")

nokluseta_v()
nokluseta_v("bbbbb")

print("Agris", "Juris", "Zane", sep=", ", end="!\n") # šādā veidā var norādīt atdalītāju un rindas beigu situāciju


def nokluseta_v2(name="Agris", sveiciens="labrīt"):
    print(f"{sveiciens} {name}")

nokluseta_v2(sveiciens="chau", name="Dace") # var darīt arī šādi, mainīt mainīgos vietām, bet tad jānorāda, kuram mainīgajam piešķir, ja nav pēc kārtas

def funkcija(*saraksts, dzeerien="ūdens"): # šādi var iedot vairākas vērtības un ja ko speciālu vēl, tad jāuzrāda ko
    for ss in saraksts:
        print(ss)

    print(dzeerien)

funkcija("kartupelis", "maize", "citrons", dzeerien="kola")

# pēc noklusējuma nevajag padot tukšu sarakstu, nav labi

def sar(elem, elem_sar=None):
    if elem_sar is None:
        elem_sar=[]
    elem_sar.append(elem)


    
    




