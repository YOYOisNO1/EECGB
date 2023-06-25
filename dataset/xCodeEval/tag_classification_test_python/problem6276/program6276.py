def program6276():
    import math
    p=10**9+7
    n=int(input())
    k=int(math.log2(n))
    f=[[n//(2**i*3**j) for j in range(3)] for i in range(k+1)]
    old=[[0,0,0] for i in range(k+1)]
    old[k][0]=1
    if n>=3*2**(k-1):
        old[k-1][1]=1
    m=n//2+2
    for i in range(2,m):
        dp=[[0,0,0] for i in range(k+1)]
        for j in range(k):
            for l in range(2):
                dp[j][l]=(old[j][l]*(f[j][l]-i+1)+old[j+1][l]*(f[j][l]-f[j+1][l])+old[j][l+1]*(f[j][l]-f[j][l+1]))%p
        old=dp
    curr=old[0][0]
    for i in range(1,n-m+2):
        curr*=i
        curr%=p
    print(curr)