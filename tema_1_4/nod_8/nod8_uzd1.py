
# 1a
def get_char_count(text):
    vardnica={}

    for ch in text:
        if ch in vardnica:
            vardnica[ch]=vardnica[ch]+1
        else:
            vardnica[ch]=1

    print(vardnica)

# text=input("Ierakstiet kaut kādu tekstu: ")
text='hubba bubba'
get_char_count(text)



# 1b
def get_digit_dict(num):
    v2={}

    for i in range(0,10):
        v2[str(i)]=0

    num_t=str(num)    
    for ch in num_t:
        if ch in v2:
            v2[ch]=v2[ch]+1
        else:
            v2[ch]=1

    print(v2)

get_digit_dict(599637003)



