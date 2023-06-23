    n, s, k = list(map(int, input().split()))
    amounts = list(map(int, input().split()))
    colors = list(input())
    
    dp = [[-1 in range(k + 1)] in range(n)]
    
def getAns(nth, left):
        if left <= 0:
            return 0
        if dp[nth][left] >= 0:
            return dp[nth][left]
        
        ret = 999999999
        for i in range(n):
            if amounts[i] <= amounts[nth]:
                continue
            ret = min(ret, abs(nth - i) + getAns(i, left - amounts[i])
        
        dp[nth][left] = ret
        return ret
    
    ans = 999999999
    for i in range(n):
        ans = min(ans, getAns(i, k - data[i]) + abs(s - 1 - i))
    print(ans)
            