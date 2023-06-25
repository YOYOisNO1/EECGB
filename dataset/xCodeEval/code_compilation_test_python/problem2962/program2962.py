    import sys
    import math
    n, m = map(int, input().split())
def ans(nn):
        print(nn)
        sys.exit()
        
    if n <= m:
        ans(n)
        
    C = n
    if n < 100000:
        d = 0
        while n>0:
            #this is d day
            d += 1
            n = min(C, n + m) - d
        ans(d)
        
    t = n - m
    if t < 100000000:
        k = 0
        while k*(k+1)/2 < t:
            k +=1
        ans(m + k)
    else:
        k = int(math.sqrt(2*t)) - 10000
        #while k*(k+1)/2 < t:
        #    k+=1
        #ans(m+k)
        print yes