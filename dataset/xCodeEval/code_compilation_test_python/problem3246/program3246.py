    import math
    
def make_digits(i,dn,s):
        l = 0
        t = set([])
        while i > 0:
            di = i % 7
            i = i / 7
            if di in s or di in t:
                return None
            else:
                t.add(di)
                l += 1
        while l < dn:
            if 0 in s or 0 in t:
                return None
            else:
                t.add(0)
                l += 1
        return t
    
    n,m = map(int,input().split(' '))
    
    dn = int(math.log(n,7)) + 1
    dm = int(math.log(m,7)) + 1
    
    count = 0
    for i in range(n):
        s = set([])
        s = make_digits(i,dn,s)
        if s == None:
            continue
        for j in range(m):
            flag = False
            t = make_digits(j,dm,s)
            if t == None:
                continue
            count += 1
    print count