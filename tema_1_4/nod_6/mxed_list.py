

mixed_list = [1, 2, 3,
              "Agris", "Programmētājs", "Ogre",
              3.14, 2.781, 0.0,
              -1, -2, -3,
              None, False, True,
              [50,2,3]]

print(mixed_list)

for item in mixed_list:
    print(item, type(item))


sum_numbers = 0
for item in mixed_list:
    if type(item) in [int, float]:
        sum_numbers+=item
    elif type(item) == list:
        for nested_item in item:
            if type(nested_item) in [int, float]:
                sum_numbers+=nested_item


print(round(sum_numbers,4))
    
print(type(5))

print(isinstance(5, int))

print(type(5) in [int, float, str])




