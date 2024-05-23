
def get_min_avg_max(sequence):
    t=tuple()
    t+=(min(sequence),)
    t+=(round(sum(sequence)/len(sequence)),)
    t+=(max(sequence),)

    return t


print(get_min_avg_max([0,10,1,9]))


# 1b
def get_min_med_max(sequence):    
    t=tuple()
    if len(sequence)%2 != 0:
        m=sorted(sequence)
        m=m[int(len(m)/2)]
    else:
        m=sorted(sequence)  
        if type(sequence)==str:
            m=m[int(len(m)/2)-1] + m[int(len(m)/2)]     
        else:
            m=(m[int(len(m)/2)-1] + m[int(len(m)/2)])/2
    
    t+=(min(sequence),)
    t+=(m,)
    t+=(max(sequence),)  
    
    return t


# print(get_min_med_max([1,5,8,4,3]))
# print(get_min_med_max([2,2,9,9,4,3]))
# print(get_min_med_max("baaac"))
print(get_min_med_max("faaacb"))


