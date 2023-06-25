    from sys import *
    setrecursionlimit(200000)
    
def il(): #Input list
        return list(map(int,input().split()))
def ii(): #Input int
        return int(input())
def imi(): #Input multiple int
        return map(int,input().split())
    p=10**9 + 7
    y=2*(10**5)
    
def power(x,y):  #x**y
        ans=1
        while(y):
            if y&1:
                ans=(ans*x)%p
                y-=1
            else:
                x = (x*x)%p
                y=y//2
        return ans
    
def powr(a,b,dp):
    
        if b==1: return a
        if b==0: return 1
        if (dp[b] > 0): return dp[b]
    
        c=powr(a,b//2,dp)
        c=(c*c)%p
        if b&1: x = (a * c) % p
        else: x=c
        dp[b] = x
        return x
    
    
    
    t=ii()
    for _ in range(t):
        n,k=imi()
    
        if k==0:
            print(1)
            continue
    
        if n&1: print(power(power(2,n-1)+1,k))
        else:
            dp=[-1]*k
            a=power(2,n-1) - 1
            b =((a+1)*2)%p
            s=power(a,k)
            y=1
            for r in range(1,k+1):
                x = powr(a, k - r,dp)
                s= (s+(x*y))%p
                y= (y*b)%p
            print(s)
    