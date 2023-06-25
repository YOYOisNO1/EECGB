def program2025():
    import sys
    sys.setrecursionlimit(10 ** 6)
    # pow(3,2,5)==4
    mod=int(1e9+7)
    # inp=input()
    n,k,d=map(int,input().split())
    """
    3
    2 1
    1 2
    1 1 1
    ---
    3
    ---
    2 1 1
    1 2 1
    3 1
    2 2
    1 1 2
    1 3
    """
    dp=[0 for i in range(150)]
    dp[1]=1
    for i in range(2,n+5):
        sum=0
        for j in range(1,k+1):
            if i-j>0:
                sum+=dp[i-j]
        dp[i]=sum
    dp2=[0 for i in range(150)]
    dp2[1]=1
    for i in range(2,n+5):
        sum=0
        for j in range(1,d):
            if i-j>0:
                sum+=dp2[i-j]
        dp2[i]=sum
    print((dp[n+1]-dp2[n+1])%mod)