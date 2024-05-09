temp=float(input("Ievadiet savu temperatūru: "))

if temp<35:
    print("nav par aukstu?")
elif temp>=35 and temp<=37:
    print("viss kārtībā!")
else:
    print("iespējams drudzis")