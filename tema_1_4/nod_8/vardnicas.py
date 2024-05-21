
# tas ir labāk, nekā lietot parasto vārdnīcu
# {} - nozīmē ka būs vārdnīca

my_dict={}
print(my_dict)

# var izmantot rezervētos vārdus, bet tas nav ieteicams: min, max, len utt...

also_empty_dict=dict() # arī tukša vārdnīca
print(also_empty_dict)

tel_dict = {"valdis":2640, "līga":2911, "pēteris":2912} # tiek piešķirta atslēga
print(tel_dict)

print("Valda tel numurs", tel_dict["valdis"])
try:
    print(tel_dict["kārlis"])
except KeyError as e:
    print("nederīga atslēga")

# jaunu ierakstu pievienošana
tel_dict["maija"]=2913
print(tel_dict)

# var pārrakstīt
tel_dict["valdis"]=2641
print(tel_dict)

# var iemest sarakstu
tel_dict["valdis"]=[2642, 2643, 2644]
print(tel_dict)
print(tel_dict["valdis"])

valda_numuri=tel_dict["valdis"]
print(valda_numuri)
print(valda_numuri[-1]) # pēdējais numurs

# pievienot jaunu numuru
valda_numuri.append(2645) # tā ir norāde, ja vajadzēja kā jaunu mainigo, tad bija jātaisa kā kopija
tel_dict["valdis"].append(2645)
print(tel_dict)
print(tel_dict["valdis"][2]) # izdrukā konkrētu vērtību

# atgriež visas atslēgas
print(tel_dict.keys())
key_list = list(tel_dict.values()) # uztaisa kopiju šajā gadījumā, pie vainas ir lists
print(key_list)

#  new_dict=dict(zip(saraskts1, saraksts2)) - no dieviem sarakstiem izveido vārdnīcu, apstāsies pie īsākā saraksta
# jāseko, lai atslēgas būtu unikālas
# pirmais elements ir atslēga, nākošais - vērtība
# var veidot vārdnīcu vārdnīcā, kā vērtību piekārtot vārdnīcu









