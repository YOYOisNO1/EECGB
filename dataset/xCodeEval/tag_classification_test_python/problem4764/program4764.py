    import copy
    
def delit(a) :
        res = []
        i = 1
        while i * i < a + 1 :
            if a % i == 0 :
                temp = [i, a // i]
                res.append(temp)
            i += 1
        return res 
        
    n = int(input())
    npr = [2,3,5,7,11,13,17,19,23,29]
    fact = delit(n)
    flen = len(fact)
    while True :
        for j in range(flen) :
            zero = 1
            if not (1 in fact[j]) and len(fact[j]) != 0 :
                zero = 0
                n1 = copy.deepcopy(fact[j])
                factj = delit(n1.pop())
                for k in range(len(factj)) :
                    factj[k].extend(n1)
                    factj[k].sort()
                    fact.append(factj[k])
            flen = len(fact)
            #print(flen,j)
        if zero == 1:
            break
    #print(fact)
    for ik in fact :
        ik.sort(reverse=True)
        if ik[-1] == 1 and len(ik) > 2:
            ik.pop()
    #fact.sort()
    j =[0]
    resj = []
    for i in fact :
        if i != j :
            resj.append(i)
        j=i
        minc = int(1e300)
    for i in resj :
        j = 0
        ss = 1
        for ii in i:
            ss *= npr[j] ** (ii-1)
            if ss > int(1e18) :
                ss = int(1e18) + 1
                break
            j += 1
        #print(ss)
        minc = min(minc,ss)
    #print(*resj)
    print(minc)