    import sys
    import math
    from bisect import bisect_left
    import heapq
    from collections import deque
    from functools import reduce
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
     
def lcm(a,b):
        return abs(a*b) // math.gcd(a, b)
    
    
def canPartition(A):
        a = reduce(lambda a, num: a|(a<<num), A, 1)
        return sum(A)%2 == 0 and a & (1 << (sum(A)//2)) != 0
     
    mod = 10**9+7
    n = II()
    a = LI()
    s = sum(a)
    ans = []
    if s%2 == 0 and canPartition(a):
        while len(ans) == 0:
            for i in range(n):
                if a[i]%2 == 1:
                    ans.append(i+1)
                    break
                else:
                    a[i]//=2
    print(len(ans))
    print(*ans)
            