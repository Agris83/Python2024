
def get_city_year(p0, perc, delta, p_target):
    i=0
    rez=p0
    
    while rez<=p_target and i>-1:
        rez=rez+rez*perc*0.01+delta
        i+=1

        if rez<=p0:
            i=-1
             
        p0=rez
        # print(rez) # - starprezultāta izdruka
    return i


# a=get_city_year(1000, 2, 50, 1200)
# a=get_city_year(1000, 2, -50, 5000)
# a=get_city_year(1500, 5, 100, 5000)
# a=get_city_year(1500000, 2.5, 10000, 2000000)

a=get_city_year(1000, -3, 40, 2000)

# ja rezultātu noapaļo uz Int - tad populācija beidzas pie 1301, bet ja atstāj Float - 1333

print(a)
