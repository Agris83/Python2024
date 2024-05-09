
furniture = "krēsls"
print(f"es sēžu uz {furniture}")
print("varbūt ir vairāki " + furniture + " -i")
paint_job = f"paņemsim un nokrāsosim {furniture}"
print(paint_job)

name = "Agris"
print(name)

x=20
y=x**2

print(f"{x} kvardrātā ir {y}")

y=5*x
print(x, y)
print(f"{y} is 5 reizes {x} tagad")
print(name, type(name))

PI=3.1415926 # iespējams, ka tā ir konstante
print(f"vērtība PI ir {PI} un datu tips ir {type(PI)}")
PI=round(PI, 4)
print(PI, type(PI))
PI=round(PI) # noapaļo līdz 0 cipariem aiz komata, veseli skaitļi
print(PI, type(PI))

some_number=5.89261
some_round_number = round(some_number)
some_int_number = int(some_number)
print(some_number, some_round_number, some_int_number)

# vidusceļu apaļo vienu uz augšu, vienu uz leju
# šajā gadījumā noapaļo tuvāk pāra skaitlim, tas ir darīts statistisku iemeslu dēļ
a=1.5
b=2.5
c=3.5
d=4.5
print(a,b,c,d)
print(round(a), round(b), round(c), round(d))

a=1.51
b=2.51
c=3.51
d=4.51
print(a,b,c,d)
print(round(a), round(b), round(c), round(d))

a=1.49
b=2.49
c=3.49
d=4.49
print(a,b,c,d)
print(round(a), round(b), round(c), round(d))


