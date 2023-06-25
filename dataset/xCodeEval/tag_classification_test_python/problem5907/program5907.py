    #!/usr/bin/env python3
    from math import gcd
    
def ri():
        return map(int, input().split())
    
def lcm(a, b):
        return a*b/gcd(a,b)
    
    
    n = int(input())
    c = list(ri())
    c = [i-1 for i in c]
    cyc = [0 for i in range(n)]
    for i in range(n):
        cc = c[i]
        s = i
        for j in range(n):
            if s == cc:
                if (j+1)%2:
                    cyc[i] = j+1
                else:
                    cyc[i] = (j+1)//2
                break
            else:
                cc = c[cc]
    
    if 0 in cyc:
        print(-1)
        exit()
    
    l = cyc[0]
    for i in range(1,n):
        l = int(lcm(l, cyc[i]))
    
    print(l)