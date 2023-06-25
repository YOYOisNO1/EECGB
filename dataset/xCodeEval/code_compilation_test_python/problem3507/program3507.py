def program3507():
    MOD = 10**9 + 7
    n,l,r = map(int,input().split())
    dp = [[0,0,0]for i in range(n+1)]
    
    # l <= x <= r を満たすｘの中で、mod 0,1,2　となる数字の個数をそれぞれa,b,cとする
    a = r//3     - (l - 1)//3
    b = (r+1)//3 - (l - 1 + 1)//3
    c = (r+2)//3 - (l - 1 + 2)//3
    #example
    #l = 2 , r = 10
    #a = 10//3 - 1//3 = 3 - 0 = 3 (3,6,9)
    #b = 11//3 - 2//3 = 3 - 0 = 3 (4,7,10)
    #c = 12//3 - 3//3 = 4 - 1 = 3 (2,5,8)
    
    dp[1][0] = a
    dp[1][1] = b
    dp[1][2] = c
    for i in range(1,n):
        dp[i+1][0] = dp[i][0]*a%MOD + dp[i][1]*c%MOD + dp[i][2]*b%MOD
        dp[i+1][1] = dp[i][0]*b%MOD + dp[i][1]*a%MOD + dp[i][2]*c%MOD
        dp[i+1][2] = dp[i][0]*c%MOD + dp[i][1]*b%MOD + dp[i][2]*a%MOD
    
    print(dp[n][0]%MOD)