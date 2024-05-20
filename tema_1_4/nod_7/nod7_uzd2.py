
# šādi definē tipus, bet Python tāpat strādās...

def is_palindrome(text: str) -> bool:
    text=text.lower()
    text=text.replace(" ","")
    rev_text=text[::-1]

    return rev_text==text # var rakstīt vnk - šādi

    # if rev_text==text:
    #     return True
    # else:
    #     return False
    
    
ievads=input("Ievadiet kaut kādu tekstu: ")
print(is_palindrome(ievads))

