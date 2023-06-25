    from collections import defaultdict, Counter,deque
    from math import sqrt, log10, log, floor, factorial,gcd
    from bisect import bisect_left, bisect_right
    from itertools import permutations,combinations
    import sys, io, os
    input = sys.stdin.readline
    # input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    # sys.setrecursionlimit(10000)
    inf = float('inf')
    mod = 10 ** 9 + 7
def get_list(): return [int(i) for i in input().split()]
def yn(a): print("YES" if a else "NO")
    ceil = lambda a, b: (a + b - 1) // b
    t=int(input())
    for i in range(t):
        n,k=[int(i) for i in input().split()]
        dp=[1 for i in range(k+1)]
        muleven=pow(2,n-1,mod)
        twon=pow(2,n,mod)
        mulodd=pow(2,n-1,mod)+1
        if n%2==0:
            for i in range(1,k+1):
                dp[i]=(dp[i-1]*(muleven-1))%mod
                dp[i]=(pow(twon,i-1,mod)+dp[i])%mod
            print(dp[-1])
        else:
            for i in range(1,k+1):
                dp[i]=(dp[i-1]*mulodd)%mod
            print(dp[-1])
    
    # 0
    # 0
    # 0
    # 0
    # 0
    # 0
    # 0
    # 5
    #
    # 0
    # 1
    # 1
    # 3*5
    #
    # 1
    # 1
    # 1
    # 5
    # 5+15+5=25