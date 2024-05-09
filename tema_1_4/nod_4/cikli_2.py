
# try:
#     num = int(input("Ierakstiet veselu sk! "))
#     print(f"drukājam {num} ir {num**2}")
# except ValueError:
#     print("kļūda!")
#     
# print("restartē programmu!")

while True:
    try:
        num = int(input("Ierakstiet veselu sk! "))
        print(f"drukājam {num} ir {num**2}")
        break # lai izietu no cikla
    except ValueError:
        print("kļūda!")
        print("mēģini vēl")
print("restartē programmu!")