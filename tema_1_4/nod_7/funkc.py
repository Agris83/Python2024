
def make_sandwich(): #funkcija
    print("aaaa")
    print("bbbb")
    print("ccccc")
    print("dddd ddd ddd")


make_sandwich() # funkcijas izsaukums

for _ in range(5): # var likt svītriņu, ja nevajag izmantot cikla mainīgo
    make_sandwich()


def make_sandwich_with(ievietots): #funkcija
    print("aaaa")
    print("bbbb")
    print(f"zzzzzzzz ar {ievietots} z zzz zzzz")
    print("ccccc")
    print("dddd ddd ddd")

make_sandwich_with("tomātiem")

def make_sandwich_with_br(plus, ievietots): #funkcija - var ielikt arī sarakstu
    print("aaaa")
    print(f"bbbb {plus}")
    print(f"zzzzzzzz ar {ievietots} z zzz zzzz")
    print("ccccc")
    print("dddd ddd ddd")

make_sandwich_with_br("maize", "tomātiem")

def make_sandwich_ar_sarakstu(plus, ievietots): #funkcija - var ielikt arī sarakstu
    print("aaaa")
    print(f"bbbb {plus}")
    for ir in ievietots:
        print(f"zzzzzzzz ar {ir} z zzz zzzz")
    print("ccccc")
    print("dddd ddd ddd")

make_sandwich_ar_sarakstu("maize", ["olas", "siers", "kartupelis"])

# strings arī var būt saraksts, ja stringa vietā pretij stāv List

def print_add(a, b):
    print(f"{a} + {b} = {a+b}")

print_add(5,6)

def reizina(a, b):
    return a*b

result = reizina(5,6)
print(result)

print_add(reizina(5,2), reizina(10,2))







