a=int(input("Ievadiet skaitli 1: "))
b=int(input("Ievadiet skaitli 2: "))
c=int(input("Ievadiet skaitli 3: "))

if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c , a, b)
else:
    print(c, b, a)

