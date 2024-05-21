
# 3a
def clean_dict_value(d, bad_val):
    new_d={}
    for key, val in d.items():
        if val!=bad_val:
           new_d[key]=val
    
    return(new_d)

print(clean_dict_value({'a':5,'b':6,'c':5}, 5))




