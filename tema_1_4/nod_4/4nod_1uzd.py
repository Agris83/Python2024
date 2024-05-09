i=1
while i<101:
    end=", "
    if i==100:
        end = " \n"
    
    if (i % 5 == 0) and (i % 7 == 0):
      #  print("Fizzbuzz", end=", ") # noņem beigu pārnesi jaunā rindā
        print("Fizzbuzz", end=end)
    elif i % 5 == 0:
        print("Fizz", end=end)
    elif i % 7 == 0:
        print("Buzz", end=end)
    else:
        print(i, end=end)
        
    i +=1
        