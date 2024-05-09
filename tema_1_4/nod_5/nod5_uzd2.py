ch=" "
find_ch=""

text=input("Ievadiet tekstu: ")

i=0
while i<2:
    new_text=""
    for letter in text:
        if letter==ch:
            new_text += letter
        else:
            if i==1:
                if letter==find_ch:
                    new_text += letter
                else:
                    new_text += "*"
            else:
                new_text += "*"
   
    print(new_text)
    if i==0:        
        find_ch=input("Ievadiet meklējamo simbolu:")
  
    i += 1
    