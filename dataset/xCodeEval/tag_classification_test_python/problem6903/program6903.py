def program6903():
    q = input()
    for _ in xrange(q):
        a, b, m = map(int, input().strip().split())
        d = b - a
        if d >= 1 and d <= m:
            print(2,) a, b
            continue
    
        if a == b:
            print(1,) a
            continue
    
        found = 0
        nval = 3
        for n in xrange(3, 51):
            exp = n - 2
            lo = (a + 1) * (1 << exp)
            hi = (a + m) * (1 << exp)
            if lo <= b and b <= hi:
                found = 1
                nval = n
                break
    
        if not found:
            print(-1)
            continue
        
        n = nval
    
        pre = [1]
        cursum = 1
        while len(pre) < n:
            pre.append(cursum)
            cursum <<= 1
    
        r = [0] * (n - 1)
    
        pre.pop()
    
        or_b = b
        b = b - a * (1 << (n - 2))
    
        stexp = 1 << (n - 2) # starting exponent
        curb = 0 # current value of b filled
        for i in xrange(n - 2):
            stexp >>= 1
            stexp = max(stexp, 1)
    
            lo = ((b - curb - pre[-1 -i] * m) + stexp - 1) // stexp
            hi = (b - curb - pre[-1 -i]) // stexp
    
            ri = max(1, lo)
            ri = min(ri, hi)
            while 1:
                if ri <= 0:
                    found = 0
                    break
    
                bfill = ri * stexp
    
                left = b - (curb + bfill)
                if left >= pre[-1 -i] and left <= pre[-1 -i] * m:
                    r[i] = ri
                    curb += bfill
                    break
                else:
                    ri -= 1
    
            if found == 0:
                break
    
        if found == 0:
            print(-1)
            continue
    
        for i in xrange(n - 2):
            assert r[i] >= 1 and r[i] <= m
            
        print(n,) a,
        rsum = a
        x = a
        for i in xrange(n - 2):
            x = rsum + r[i]
            print(x,) 
            rsum += x
        assert or_b - rsum >= 1 and or_b - rsum <= m
        print(or_b,)
        print