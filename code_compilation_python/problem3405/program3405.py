def program3405():
    import math
    
    ans = 0
    n = int(input())
    sq = int(math.sqrt(n))
    pythagDict = {}
    for x in range(1,sq+2):
        for y in range(1,x):
            a = 2*x*y
            b = x*x-y*y
            c = x*x+y*y
            pair = [min(a,b),max(a,b)]
            if c not in pythagDict and c <= n:
                pythagDict[c] = [pair]
                ans += 1
            elif c <= n:
                if pair not in pythagDict[c]:
                    pythagDict[c].append(pair)
                    ans += 1
    for i in pythagDict:
        for pair in pythagDict[i]:
            for k in range(2,n/i):
                if k*i not in pythagDict:
                    pythagDict[k*i] = [[pair[0]*k,pair[1]*k]]
                    ans += 1
                elif [pair[0]*k,pair[1]*k] not in pythagDict[k*i]:
                    pythagDict[k*i].append([pair[0]*k,pair[1]*k])
                    ans += 1
    print ans