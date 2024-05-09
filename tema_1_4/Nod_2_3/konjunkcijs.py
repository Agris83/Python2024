is_raining=False
is_spring=True
is_sunny=True

print(is_spring and is_sunny)

# konjunkcija
print("False and False",False and False)
print("False and True",False and True)
print("True and False",True and False)
print("True and True",True and True)

print(True and True and True and True and 2*2==4)
print(False and True and 5/0==500) # slinkā valoda, apstājas pie pirmā False

# disjunkcija
print("False or False",False or False)
print("False or True",False or True)
print("True or False",True or False)
print("True orr True",True or True)

print(False or False or True or 5/0 == 500)

a=2
b=4
c=10

print(a<b<c)
print(a<b and b<c)

# negācija

print("reverse of is_raining?", not is_raining)
