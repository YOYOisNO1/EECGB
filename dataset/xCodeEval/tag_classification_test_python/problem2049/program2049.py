def calculateWays(summ, maxNumber):
        p = [0] * (summ + 1)
        dp = []
        for i in range(summ + 1):
            dp.append(p.copy())
        for i in range(summ):
            for j in range(summ):
                x = i + 1
                y = j + 1
                if x <= y:
                    prevWays = 0
                    for ii in range(y - 1):
                        if ii < maxNumber:
                            prevWays = (prevWays + dp[x - 1][y-ii-1])%1000000007
                    if y <= maxNumber and x == 1:
                        dp[x][y] = (prevWays + 1)%1000000007
                    else:
                        dp[x][y] = prevWays%1000000007
        # for i in range(summ + 1):
        #     print(dp[i])
        ans = 0
        for i in range(summ):
            ans = ans + dp[i+1][summ]
        return ans
    
    
def main():
        n,k,d = list(map(int,input().split()))
        print((calculateWays(n,k)-calculateWays(n,d-1))%1000000007)
    
    main()