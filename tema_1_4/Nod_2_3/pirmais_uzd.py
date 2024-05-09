import datetime

name=input("Kāds ir Jūsu vārds? ")
age=input(f"{name} kāds ir Jūsu vecums? ")
kad100=100-int(age)
print(f"{name} pēc {kad100} gadiem Jums būs 100 gadi!")
currentYear=datetime.datetime.now().year
gads100=currentYear + kad100
print(f"{name} 100 gadi Jums paliks {gads100}")