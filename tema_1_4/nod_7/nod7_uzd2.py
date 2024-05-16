
def is_palindrome(text):
    text=text.lower()
    text=text.replace(" ","")
    rev_text=text[::-1]

    if rev_text==text:
        return True
    else:
        return False
    
    
ievads=input("Ievadiet kaut kādu tekstu: ")
print(is_palindrome(ievads))

