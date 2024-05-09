
for i in range(5):
    print("i ir ", i)
    
print("beigās i ir: ", i)


for i in range(10,15):
    print("i ir ", i)
    
print("beigās i ir: ", i)


for i in range(30,50,2):
    print("i ir ", i)
    
print("beigās i ir: ", i)

for i in range(100,90,-2):
    print("i ir ", i)
    
print("beigās i ir: ", i)

name = "Agris"
for c in name:
    print("vārdu mainīgie", c)
    
for i, c in enumerate(name):
    print("vārdu mainīgie", i, c, ord(c))  
    
    
for i in range(10):
    print(i)
    if i == 4044:
        print("ir 4", i)
        break
else:
    print("finālā", i)
print("pēc cikla:", i)
    