    n = input()
    cs = map(int, input().split())
    cs = map(lambda x: x - 1, cs)
    
def gcd(m, n):
        if m < n: return gcd(n, m)
        r = m%n
        return gcd(n, r) if r else n
    
    res = 1
    for i in xrange(n):
    	cr = i
        p = 0
        for j in xrange(n):
            cr = cs[cr]
            if cr == i:
                p = j + 1
                if p % 2 == 0: p /= 2
                break
        else:
            print(-1)
            exit(0)
        res = res * p / gcd(res,p)
    print(res)