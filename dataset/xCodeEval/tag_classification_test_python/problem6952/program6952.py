    import sys
    input = sys.stdin.readline
    from collections import *
    from math import gcd
    
def lcm(x, y):
        return x*y//gcd(x, y)
    
    n = int(input())
    ans = 0
    MOD = 10**9+7
    
    for c in range(1, n-1):
        divs = []
        
        for d in range(1, int((n-c)**0.5)+1):
            if (n-c)%d==0:
                divs.append(d)
                
                if d!=(n-c)//d:
                    divs.append((n-c)//d)
        
        divs.sort(reverse=True)
        cnts = []
        
        for i in range(len(divs)):
            cnt = (n-c-1)//divs[i]
            
            for j in range(i):
                if divs[j]%divs[i]==0:
                    cnt -= cnts[j]
            
            cnts.append(cnt)
            ans += lcm(c, divs[i])*cnt
            ans %= MOD
            
    print(ans)