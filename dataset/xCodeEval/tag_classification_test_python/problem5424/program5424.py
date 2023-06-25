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
    
def powr(a,b,dp):
    
        if b==0: return 1
        if b==1: return a
        if (dp[b] > 0): return dp[b]
        x = (powr(a, b//2, dp) * powr(a, b - b//2, dp)) % p
        dp[b] = x
        return x
    
    dp=[-1]*(y+1)
    
    t=ii()
    for _ in range(t):
        n,k=imi()
    
        if (n&1)==0:
            dp2=[-1]*(k+1)
            dp3=[-1]*(k+1)
            a=powr(2,n,dp)
    
            s=0
            dp3[0]=1
            x=powr(2,n-1,dp)
            z= (x*2)%p
    
            for i in range(1,k+1):
                dp3[i]= ((x-1)*dp3[i-1] + powr(z,i-1,dp2))%p
            print(dp3[k])
        else:
            a=powr(2,n-1,dp)+1
            dp4=[-1]*(k+1)
            s=powr(a,k,dp4)
            print(s)
    
    
    