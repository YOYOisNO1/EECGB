    from sys import stdin
    input = stdin.readline
    
    inp = lambda : list(map(int,input().split()))
    
def add(a , b):return ((a%mod) + (b%mod))%mod
def sub(a , b):return (a - b + mod)%mod
def mul(a , b):return ((a%mod) * (b%mod))%mod
def ncr(n , r):
        if(r > n):return 0
        return mul(fact[n] , mul(facti[n - r] , facti[r]))
def div(a , b):return mul(a , pow(b , mod - 2 , mod))
    
    
    """
    
    select x continuous things then a hole
    
    dp[i][j] => i elements which I can select
             => j active holes
    
    """
    
def solve(i , j):
    
        if(j < 0):return 0
    
        if(i == 0):
            if(j == 0):return 1
            else:return 0
    
        if(dp[i][j] != -1):return dp[i][j]
    
        ans = 0
        for x in range(1 , i + 1):
    
            ways = p[x - 1]
            ways = mul(ways , comb[i][x])
            ans = add(ans , mul(ways , solve(i - x , j - 1)))
    
        dp[i][j] = ans
        return ans
        
    
def answer():
    
        global dp
        dp = [[-1 for i in range(n + 1)] for j in range(n + 1)]
    
        ans = 0
        for i in range(n):
            ans = add(ans , solve(n - i , i + 1))
    
        return ans
    
    for T in range(1):
    
        n , mod = inp()
        fact , facti , p = [1] , [1] , [1]
        size = 2 * (10**3) + 1
        for i in range(1 , size):
            fact.append(mul(fact[-1] , i))
            facti.append(pow(fact[-1] , mod - 2 , mod))
            p.append(mul(p[-1] , 2))
    
        comb = [[0 for i in range(1001)] for j in range(1001)]
    
        for i in range(1 , 1001):
            for j in range(1 , 1001):
                comb[i][j] = ncr(i , j)
    
        print(answer())