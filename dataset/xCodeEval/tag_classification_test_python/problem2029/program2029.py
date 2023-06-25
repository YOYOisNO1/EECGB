    
    dp = []
    
def f(n, k, d):
        global dp
        if n < 0:
            return 0
        if n == 0 and d == 0:
            dp[n][k][d] = 1
            return 1
    
        if dp[n][k][d] != -1:
            return dp[n][k][d]
    
    
        cont = 0
        for i in range(1, k+1):
            cont += f(n-i, k, 0 if i>=d else d)
        dp[n][k][d] = cont
        return cont
    
    
    
    
def main():
        global dp
        n, k, d = [int(i) for i in input().split()]
        dp = [[[-1 for j2 in range(d+1)] for j in range(k+1)] for i in range(n+1)]
        print(f(n, k, d) % 1000000007 )
        return
    
    
    main()
    