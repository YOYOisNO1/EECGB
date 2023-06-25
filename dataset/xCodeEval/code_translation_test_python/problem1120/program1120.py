def program1120():
    p, k = map(int, input().split())
    
    l = [0]
    r = [0]
    cp = [1]
    coef = []
    
    for deg in range(1, 2333):
        l.append(l[-1])
        r.append(r[-1])
        if cp[-1] > 0: r[-1] += cp[-1] * (k-1)
        else : l[-1] += cp[-1] * (k-1)
        if p <= r[-1] and p >= l[-1]:
            coef = [0] * deg
            break
        cp.append(cp[-1] * (-k))
    
    cv = p
    for deg in range(len(coef), 0, -1):
        if cv >= l[deg-1] and cv <= r[deg-1]: continue
        elif cv > r[deg-1]:
            coef[deg-1] = (cv - r[deg-1]) // cp[deg-1]
            if((cv-r[deg-1]) % cp[deg-1] != 0):
                coef[deg-1] += 1
            cv -= cp[deg-1] * coef[deg-1]
        elif cv < l[deg-1]:
            coef[deg-1] = (l[deg-1] - cv) // -cp[deg-1]
            if((l[deg-1]-cv) % -cp[deg-1] != 0):
                coef[deg-1] += 1
            cv -= cp[deg-1] * coef[deg-1]
    
    print(len(coef))
    print(" ".join(map(str, coef)))