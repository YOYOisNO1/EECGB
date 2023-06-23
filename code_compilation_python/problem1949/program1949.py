    #!/usr/bin/env python3
    import io
    import os
    import sys
    
    input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    
def printd(*args, **kwargs):
        #print(*args, **kwargs, file=sys.stderr)
        #print(*args, **kwargs)
        pass
    
def get_str():
        return input().decode().strip()
    
def rint():
        return map(int, input().split())
    
def oint():
        return int(input())
    
    mod = 1000000007
    n, a, b, k = rint()
    if a > b:
        a, b = n-a+1, n-b+1
    a -= 1
    b -= 1
    
    d = [0]*n
    d[a] = 1
    ps = [0]*b
    ps[0] = d[0]
    for j in range(1, b):
        ps[j] = ps[j-1]+d[j]
    printd(n, a, b, k)
    printd(d, ps)
    for i in range(k):
        for j in range(b):
            #b-t > t-j
            #2*t < b+j
            #t < (b+j)/2
            if (b+j)%2:
                t = (b+j)//2
            else:
                t = (b+j)//2 - 1
            d[j] = ps[t] - ps[j]
        for j in range(1, b):
            d[j] += ps[j-1]
        ps[0] = d[0]
        for j in range(1, b):
            ps[j] = (ps[j-1]+d[j])%mod
        printd(d,ps)
    
    print(ps[b-1]%mod)