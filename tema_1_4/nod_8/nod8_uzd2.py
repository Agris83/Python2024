
def replace_dict_value(d, bad_val, good_val):

    for key, val in d.items():
        if val==bad_val:
            d[key]=good_val

    return(d)

print(replace_dict_value({'a':5,'b':6,'c':5}, 5, 10))
