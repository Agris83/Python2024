
saraksts=[]
elem=""

while elem !="q":
    try:
        elem=input("Ievadiet skaitli vai q: ")
        saraksts.append(float(elem))        
        print(f"ievadīto skaitļu vidējā vērtība: {round(sum(saraksts)/len(saraksts),2)}")
        print(f"Pirmie 3 sk: {saraksts[:3]} un pēdējie 3 sk: {saraksts[-3:]}")
    except ValueError:  
        continue
        


