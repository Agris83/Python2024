a=200
b=4

if a<b:
    print("a < b ", a<b)
    print("a ir", a)
    print("b ir", b)
    
    
print("programma palaidās")

if a>b:
    print("kaut kas")
    print(a,b)
else:
    print("nesanāca iepriekšējais")
    print(a,b)
        
# if iekš IF
c=100
d=200
f=300

if a>b:
    print("cool a > b", a, b)
    if c<d:
        print("aha c<d", c,d)
    else:
        print("oho c>=d", c, d)
else:
    print("means a <=b", a, b)
    if c<d<f:
        print("cool c<d<f", c, d, f)
    else:
        print("apparently NOT c<d<f", c<d,f)
        
# vēl viens variants
# flat if else
a=4
print("cheks")
if a>b:
    print("a>b", a, b)
elif a<b:
    print("a<b", a, b)
else:
    print("visi atlikušie gadījumi", a, b)

print("ok")