
import requests
import json

url = "https://dummyjson.com/recipes"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(data)

print(data.keys())

recipes = data['recipes']

print(len(recipes))

rp_list=[]
for rp in recipes:
    potato=False
    for ingredient in rp["ingredients"]:
        if ingredient[:6].lower() =="potato": # var arī rakstīt if "potato" in ingredient
            potato=True
            break
    if potato==True:
        rp_list.append(rp)
    
print(len(rp_list))

for ediens in rp_list:
    print(ediens["name"])

print(type(rp_list))

with open('nod_14\\receotes.json', 'w') as file:
    json.dump(rp_list, file, indent=1)



