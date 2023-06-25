def program4722():
    q = int(input())
    initialQ = q
    d = {}
    i = 2
    
    while i * i <= q:
        if q % i:
            i += 1
            continue
        d[i] = 0
        while q % i == 0:
            q //= i
            d[i] += 1
        i += 1
    
    if q != 1 and q != initialQ:d[q] = 1
    
    l = sum(d[item] for item in d)
    
    newD = []
    for item in d:
        newD += [item] * d[item]
    
    if l > 2:
        print(1)
        print(newD[0] * newD[1])
    elif l == 2:
        print(2)
    else:
        print(1)
        print(0)