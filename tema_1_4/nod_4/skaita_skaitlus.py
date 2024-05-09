
total=0
user_input=""
while user_input !="q":
    try:
        user_input=input("ievadiet ciparu vai q:")
        number=float(user_input)
    except ValueError:
        if user_input != "q":
            print("ievadiet skaitli")
        continue
    total += number
    print("ievadīts", number)
    print("total ir tagad", total)