def program2037():
    import math as mt 
    import sys,string
    input=sys.stdin.readline
    import random
    from collections import deque,defaultdict
    L=lambda : list(map(int,input().split()))
    Ls=lambda : list(input().split())
    M=lambda : map(int,input().split())
    I=lambda :int(input())
    n,k,d=M()
    
    3
    dp=[0]*(n+1)
    dp[0]=1
    dp2=[0]*(n+1)
    dp2[0]=1
    for i in range(1,n+1):
        for j in range(1,k+1):
                if(i-j>=0):
                    dp[i]+=(dp[i-j])
    for i in range(1,n+1):
        for j in range(1,d):
            if(i-j>=0):
                dp2[i]+=(dp2[i-j])
    
    print((dp[n]-dp2[n])%(10**9+7))