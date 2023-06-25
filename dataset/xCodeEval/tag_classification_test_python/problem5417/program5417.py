    import sys
    input=sys.stdin.readline
    INF=int(1e9)+7
    
def power(x, y):
        if y == 0:
            return 1
        semi_result = power(x, y // 2)%INF
        
        if y % 2 == 0:
            return (semi_result * semi_result)%INF
        else:
            return (x * semi_result * semi_result)%INF
        
    for _ in range(int(input())):
        n,k=map(int,input().split())
        dp=[1]*(k+1)
        g=power(2,n-1)
        a=(g*2)%INF
        cache=[1]*(k+1)
        for i in range(2,k+1):
            cache[i]=(cache[i-1]*a)%INF
        for i in range(1,k+1):
            if n%2==0:
                dp[i]=(cache[i]+dp[i-1]*(g-1))%INF
            else:
                dp[i]=(dp[i-1]+g*dp[i-1])%INF
        print(dp[k])