

print("Labdien...")

i = 0
while i<5:
    print("drukāju i: ", i)
    i+=1    

print("fināla i bez cikla: ", i)


floor=9

while floor>=0:
    print(f"kāpju lejā uz {floor} stāvu")
    floor-=1
print(f"esmu ticis {floor} stāvā!")

cnt=10
while cnt<=20:
    print(f"cnt is {cnt}")
    cnt+=2
print(f"fināla cnt ir {cnt}")

start=100
stop=200
step=25

i=start
while i<stop:
    print(f"drukāju {i}")
    i+=step
print(f"gala i = {i}")

i=0
while i<10:
    print("i is", i)
    i+=1
    if i>5:
        print("pauze")
        break
    print("ir ciklā: ", i)
print("fināla vērtība", i)


i=0
import random
while i<10_000:
    dice_throw=random.randint(1,6)
    if dice_throw==6:
        print("supper, ir seši", dice_throw)
        print("brīvais", i)
        break
    i+=1
print("ok", i)
    
    
    

