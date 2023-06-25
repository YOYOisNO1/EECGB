def play(price, n):
        # dp[i][j][k] -  наименьшая стоимость перемещения i блинов со стержня j => k
        # У нас всегда есть два варианта действия:
        # 1. Перемещаем i - 1 блин на место 2. Далее, перемещаем i - ый блин на место 3. И наконец перемещаем i - 1 блин на место 3.
        # 2. Перемещаем i - 1 блин на место 3. Затем i - ый на место 2, затем i - 1 блин на место 1, далее i -ый на 3-е место и наконец i - 1 блин на 3 место
        # т.е, dp[i][j][k] = min(dp[i - 1][j][k ^ j] + Price[j][k] + dp[i - 1][k ^ j][k], 
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