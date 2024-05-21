
food_prices = {'ābols':0.99, 'banāns':0.59, 'apelsīns':0.79}

needle = 'banāns'

if needle in food_prices:
    print(f"cena {needle} ir {food_prices[needle]}")
else:
    print("ņav")


needle = 'kiwi'

price=food_prices.get('banāns')
print(f"cena banānam ir {price}")

price=food_prices.get('kiwi')
print(f"cena kiwi ir {price}")

# get metodē iekšā ir IF

# setdefault -
price=food_prices.setdefault('kiwi', 1.99)
print(f"cena kiwi ir {price}")

print(food_prices)

food_prices['kiwi']=3.50
print(food_prices['kiwi'])

price=food_prices.setdefault('kiwi', 1.99) # ja nav šāda elementa, tad atgriezīs norādīto
print(f"cena kiwi ir {price}")

# del
# pop 
food_prices.pop("banāns")

food_prices.clear() # izmet visu ārā
# food_prices.popitem() # izmet random vērtību

# update - apdeito vērtības vārdnīca ar vārdnīcu, jaunās pieveino, esošās pārraksta

new_dict={}
new_dict={'ābols':1, 'banāns':2, 'kiwi':3}
new_dict.fromkeys(['ābols', 'banāns', 'kiwi'], 0.99) # pieliek visiem vienu vārdnīcu, noder sākuma vērtībām
print(new_dict)

# funkcijās 
# def abc(**abc): - šādi var padot veselu kaudzi ar atslēgām



