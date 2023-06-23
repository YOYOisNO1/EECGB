    # This code is contributed by Siddharth
    
    from sys import *
    input = stdin.readline
    
    
    
    
    import random
    from bisect import *
    import math
    from collections import *
    import operator
    from heapq import *
    from itertools import *
    inf=10**18
    mod=10**9+7
    
    # inverse modulo power pow(a,-1,mod) - it only works on py 3.8 ( *not in pypy )
    
    
    
    # ==========================================> Code Starts Here <=====================================================================
    
    
    
def solve(x):
        if dp[x]!=-1:
            return dp[x]
        if x<=1:
            dp[x]=0
            return 0
        if x==2:
            dp[x]=2
            return 2
        ans=0
        for i in range(1,x):
            ans=(ans+max(1,solve(x-i)))%m
        for i in range(2,x+1):
            if i>x:
                continue
            ans=(ans+max(1,solve(x//i)))%m
        dp[x]=ans%m
        return dp[x]
    
    
    
    n,m=map(int,input().split())
    dp=[-1]*(n+5)
    print(solve(n)%m)
    
    
    
    
    
    
    
    
    
    