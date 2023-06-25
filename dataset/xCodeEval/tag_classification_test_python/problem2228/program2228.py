def program2228():
    import sys
    from math import *
    readints=lambda:map(int, input().strip('\n').split())
    
    
    n = int(input())
    
    s = int(sqrt(n))
    
    ans = s+s
    
    n -= s*s
    
    ans += ceil(n/s)
    
    print(ans)