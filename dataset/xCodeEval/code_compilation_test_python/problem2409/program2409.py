    from __future__ import division, print_function
    import sys
    if sys.version_info[0] < 3:
        from __builtin__ import xrange as range
        from future_builtins import ascii, filter, hex, map, oct, zip
        
    import sys, os.path
    from collections import*
    from copy import*
    import math
    mod=10**9+7
    if(os.path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")   
    
    
    sys.setrecursionlimit(10**6)
    from types import GeneratorType
def bootstrap(func, stack=[]):
    def wrapped_function(*args, **kwargs):
            if stack:
                return func(*args, **kwargs)
            else:
                call = func(*args, **kwargs)
                while True:
                    if type(call) is GeneratorType:
                        stack.append(call)
                        call = next(call)
                    else:
                        stack.pop()
                        if not stack:
                            break
                        call = stack[-1].send(call)
                return call
        return wrapped_function
    
    n, k = [int(i) for i in input().split()]
    dp = [[-1]*(2005) for i in range(2005)]
    MOD=10**9+7
def solve(x,k):
        if(k==0):
            return 1
        elif(dp[x][k]!=-1):
            return dp[x][k]
        ans=0
        for i in range(x,n+1,x):
            ans+=solve(i,k-1)
        dp[x][k]=ans%MOD
        return dp[x][k]
    res=solve(1,k)
    print(res)
     
    
    