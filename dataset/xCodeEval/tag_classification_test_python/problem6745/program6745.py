    import math
    
def solve(n,k,s,t):
    
    
        #dont change the current character
        #change the current character to t0
        #change the current character to t1
    
        dp = [[[-1*math.inf for i in range(n+1)] for j in range(n+1)] for z in range(n+1)]
        dp[0][0][0] = 0
    
        for i in range(n):
            for ck in range(k+1):
                for cnt0 in range(n+1):
                    if dp[i][ck][cnt0] == -1*math.inf: continue
                    e0 = s[i] == t[0]
                    e1 = s[i] == t[1]
                    e01 = t[0] == t[1]
    
                    #first transition
                    if e1 == True: temp1 = cnt0
                    else: temp1 = 0
                    dp[i+1][ck][cnt0+e0] = max(dp[i+1][ck][cnt0+e0], dp[i][ck][cnt0] + temp1)
    
                    if ck < k:
                        #second transition
                        if e01 == True: temp01 = cnt0
                        else: temp01 = 0
                        dp[i+1][ck+1][cnt0+1] = max(dp[i+1][ck+1][cnt0+1], dp[i][ck][cnt0] + temp01)
                        #third transition
                        dp[i+1][ck+1][cnt0+e01] = max(dp[i+1][ck+1][cnt0+e01], dp[i][ck][cnt0] + cnt0)
    
        ans = 0
    
        for ck in range(k+1):
            for cnt0 in range(n+1):
                ans = max(ans, dp[n][ck][cnt0])
    
        print(ans)
    
    
    
    
    
    
    if __name__ == '__main__':
        n,k = map(int,input().split())
        s = input()
        t = input()
        solve(n,k,s,t)