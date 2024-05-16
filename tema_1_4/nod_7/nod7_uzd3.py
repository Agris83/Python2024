
def get_city_year(p0, perc, delta, p_target):
    i=0
    rez=p0
    
    while rez<=p_target and i>-1:
        rez=rez+rez*perc*0.01+delta    
        i+=1

        if rez<=p0:
            i=-1

    return i


a=get_city_year(1500, 5, 100, 5000)

print(a)

