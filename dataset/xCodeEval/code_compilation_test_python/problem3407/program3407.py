def program3407():
    import math
    
    n = int(input())
    sq = int(math.sqrt(n))
    pythagList = []
    for k in range(1,2+n/3):
        for x in range(1,sq+1):
            for nyin range(1,m):
                a = 2*k*m*n
                b = k*(m*m-n*n)
                c = k*(m*m+n*n)
                l = [a,b,c]
                l.sort()
                if l not in pythagList and c <= n:
                    pythagList.append(l)
    print len(pythagList)