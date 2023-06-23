def play(price, n):
        # dp[i][j][k] -  naimen'shaya stoimost' peremeshcheniya i blinov so sterzhnya j => k
        # U nas vsegda est' dva varianta dejstviya:
        # 1. Peremeshchaem i - 1 blin na mesto 2. Dalee, peremeshchaem i - yj blin na mesto 3. I nakonec peremeshchaem i - 1 blin na mesto 3.
        # 2. Peremeshchaem i - 1 blin na mesto 3. Zatem i - yj na mesto 2, zatem i - 1 blin na mesto 1, dalee i -yj na 3-e mesto i nakonec i - 1 blin na 3 mesto
        # t.e, dp[i][j][k] = min(dp[i - 1][j][k ^ j] + Price[j][k] + dp[i - 1][k ^ j][k], 
        # dp[i - 1][j][k] + Price[j][k ^ j] + dp[i - 1][k][j] + Price[j ^ k][k] + dp[i - 1][j][k])
    
        dp = [[[0 for k in range(0, 4)] for j in range(0, 4)] for i in range(0, n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, 4):
                for k in range(1, 4):
                    dp[i][j][k] = min(dp[i - 1][j][k ^ j] + price[j][k] + dp[i - 1][k ^ j][k], 2 * dp[i - 1][j][k] + price[j][k ^ j] + dp[i - 1][k][j] + price[j ^ k][k])
    
        return dp[n][1][3]
    
    
def main():
        matrix = [[0 for j in range(0, 4)] for i in range(0, 4)]
        i = 1
        while i < 4:        
            row = list(map(int, input().split()))   
            for j in range(1, 4):
                matrix[i][j] = row[j - 1]
            i += 1
    
        n = int(input())
    
        print(play(matrix, n))
        
    main()
    #print(play([[0, 0, 0, 0], [0, 0, 1, 1],[0, 1, 0, 1],[0, 1, 1, 0]], 3))