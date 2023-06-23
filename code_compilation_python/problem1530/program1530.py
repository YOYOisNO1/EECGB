    from math import *
    from sys import *
    
    N=int(input())
    
    # if N <= 7:
    #     print(N,N)
    # elif N <= 15:
    #     print(N-7,N)
    # elif N <= 23:
    #     print(N-14,N)
    # else:
    
    memo={}
    
def solve(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0,0
        s=floor(pow(n,1/3)-1)
        while (s+1)**3 <= n:
            s += 1
        A,B=solve(n - s ** 3)
        C,D=solve(s**3-1)
        memo[n] = max((A+1,B+s**3),(C,D))
        #print(n, A, B, C, D, memo[n])
        return memo[n]
    
    i=1
    while i**3 < N:
        solve(i**3)
        i+=1
    
    A,B=solve(N)
    print(A,B)