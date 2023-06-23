def is_sat(candi, cont):
        candi_match = cont[0]
        _bcount = int(cont[1])
        _ccount = int(cont[2])
        bcount = 0
        ccount = 0
        for i in xrange(4):
            if candi_match[i] == candi[i]:
                bcount += 1
            elif candi_match[i] in candi:
                ccount += 1
        return (_bcount == bcount and _ccount == ccount)
        
    constraints = []
    
    N = int(input())
    while N>0:
        constraints.append([x for x in input().split()])
        N-=1
    satisfies = []
    for i in xrange(0,10000):
        candi = str(i).rjust(4,'0')
        satcount = 0
        for cont in constraints:
            if is_sat(candi, cont):
                satcount+=1
        if satcount == len(constraints):
            satisfies.append(candi)
            
    goo = len(satisfies)
    if goo  == 1:
        valid = True
        for i in xrange(4):
            for j in xrange(4):
                if i!=j:
                    if satisfies[i]==satisfies[j]:
                        valid=False
                        break
        if valid:
            print satisfies[0]
        else:
            print "Incorrect data"
    elif goo == 0:
        print "Incorrect data"
    else:
        print "Need more data"