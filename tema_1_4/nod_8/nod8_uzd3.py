
# 3a
def clean_dict_value(d, bad_val):
    new_d={}
    for key, val in d.items():
        if val!=bad_val:
           new_d[key]=val
    
    return(new_d)

print(clean_dict_value({'a':5,'b':6,'c':5}, 5))

# 3a
def clean_dict_values(d, bad_sar):
    d_kopy=d.copy()

    for key, val in d.items():
        for dd in bad_sar:
            if val==dd:
                if key in d_kopy:
                    del d_kopy[key]
    return(d_kopy)

print(clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]))
