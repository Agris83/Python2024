precizitate=2

alga=float(input("Kāda ir Jūsu mēnešalga? EUR "))
gadi=int(input("Kāds ir Jūsu nostrādāto gadu skaits? "))

if gadi>2:
    bonuss=round(((alga*15)/100)*(gadi-2), precizitate)
    print(f"Jums tiks pieškirts bonuss EUR {bonuss} apmērā!")
else:
    print("Diemžēl, Jums bonus NAV paredzēts!")