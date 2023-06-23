    import sys
    import math
def II():
    	return int(sys.stdin.readline())
     
def LI():
    	return list(map(int, sys.stdin.readline().split()))
     
def MI():
    	return map(int, sys.stdin.readline().split())
     
def SI():
    	return sys.stdin.readline().strip()
    
def FACT(n, mod):
        s = 1
        facts = [1]
        for i in range(1,n+1):
            s*=i
            s%=mod
            facts.append(s)
        return facts[n]
    
def C(n, k, mod):
        return (FACT(n,mod) * pow((FACT(k,mod)*FACT(n-k,mod))%mod,mod-2, mod))%mod
    
    n,x,pos = MI()
    
    left = 0
    right = n
    less = 0
    more = 0
    while left<right:
        middle = (left+right)//2
        if middle<=pos:
            if middle<pos:
                less+=1
            else:
                break
            left = middle+1
        else:
            more+=1
            right = middle
    hasLess = x-1
    hasBig = n-x
    if less>hassLess or more > hasBig:
        print(0)
    else:
        mod = 10**9+7
        ans = FACT(less,mod)*C(hasBig, more, mod)%mod
        ans = ans*FACT(more,mod)%mod
        ans = ans*C(hasLess, less, mod)%mod
        ans*=FACT(n-less-more-1, mod)
        ans%=mod
        print(ans)
        
    