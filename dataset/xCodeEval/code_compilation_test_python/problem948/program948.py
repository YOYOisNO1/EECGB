    import sys
    input=sys.stdin.readline
    INF=int(1e9)+7
    
def power(x, y):
        if y == 0:
            return 1
    
        # 계산을 한 번만 하기 위해서 변수에 저장
        semi_result = power(x, y // 2)%INF
        
        # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
        if y % 2 == 0:
            return (semi_result * semi_result)%INF
        else:
            return (x * semi_result * semi_result)%INF
        
    for _ in range(int(input())):
        n,k=map(int,input().split())
        dp=[1]*(k+1)
        g=power(2,n-1)
        a=(g*2)%INF
        for i in range(1,k+1):
            if n%2==0:
                dp[i]=(power(a,i-1)+dp[i-1]*(g-1))%INF
            else:
                dp[i]=(dp[i-1]+g*dp[i-1])%INF
        print(dp[k])