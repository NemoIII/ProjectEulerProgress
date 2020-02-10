def evenfibSum1(limit) :
    ef1 = 0
    ef2 = 2
    sm = ef1+ef2
    while(ef2 < limit) :
        ef3 = 4 * ef2 + ef1
        ef1 = ef2
        ef2 = ef3
        if ef3 < limit :
            sm = sm + ef3
    return sm

# executing
limit = 40000
print(evenfibSum1(limit))


