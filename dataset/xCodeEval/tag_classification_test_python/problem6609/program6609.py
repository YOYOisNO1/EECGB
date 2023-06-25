    from sys import stdin, stdout
    from collections import Counter, defaultdict
    from itertools import permutations, combinations
    input = stdin.readline
    pr = stdout.write
    
    
def in_num():
        return int(input())
    
    
def in_arr():
        return map(int,input().split())
    
    
def pr_num(n):
        stdout.write(str(n)+'\n')
    
    
def pr_arr(arr):
        pr(' '.join(map(str,arr))+'\n')
    
    # fast read function for total integer input
    
def inp():
        # this function returns whole input of
        # space/line seperated integers
        # Use Ctrl+D to flush stdin.
        return map(int,stdin.read().split())
    
    range = xrange # not for python 3.0+
    mod=10**9+7
    n,a,b,k=in_arr()
    dp=[[0 for i in range(n+1)] for j in range(k+1)]
    dp[0][a-1]=1
    dp[0][a]=(-1)%mod
    b-=1
    for i in range(k):
        temp=0
        for j in range(n):
            temp=(temp+dp[i][j])%mod
            
            x=int(abs(b-j))
            x-=1
            if x<=0:
                continue
            dp[i+1][max(0,j-x)]=(dp[i+1][max(0,j-x)]+temp)%mod
            dp[i+1][min(n,j+x+1)]=(dp[i+1][min(n,j+x+1)]-temp)%mod
            dp[i+1][j]=(dp[i+1][j]-temp)%mod
            dp[i+1][j+1]=(dp[i+1][j+1]+temp)%mod
            
    ans=0
    temp=0
    for i in range(n):
        temp+=dp[k][i]
        temp%=mod
        ans+=temp
        ans%=mod
    pr_num(ans)
    
                