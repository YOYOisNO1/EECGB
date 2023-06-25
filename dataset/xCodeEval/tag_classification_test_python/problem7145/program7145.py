    from sys import stdin
    input = stdin.readline
    
    
    inp = lambda : list(map(int,input().split()))
    
    mod = 998244353
def add(a , b):return ((a%mod) + (b%mod))%mod
def sub(a , b):return (a - b + mod)%mod
def mul(a , b):return ((a%mod) * (b%mod))%mod
    
def ncr(n , r):
        if(n < r):return 0
        return mul(fact[n] , mul(facti[n - r] , facti[r]))
    
def div(a , b):return mul(a , pow(b , mod - 2 , mod))
    
    fact , facti = [1] , [1]
    size = 2 * (10**5) + 1
    for i in range(1 , size):
        fact.append(mul(fact[-1] , i))
        facti.append(pow(fact[-1] , mod - 2 , mod))
    
    c = [[-1 for i in range(251)] for j in range(251)]
    for i in range(251):
        for j in range(251):
            c[i][j] = ncr(i , j)
    
    
def solve(i , j):
    
        if(i < 0):return 0
        if(i == 0 and j == 0):return 1
        if(dp[i][j] != -1):return dp[i][j]
    
        #picking nodes of weights (k + 1) only
        ans = 0
        for count in range(j + 1):
    
            pairs = (count * (count - 1))//2
            pairs += count * (j - count)
    
            ways = c[j][count]
            power = pow(k - i + 1 , pairs , mod)
            toadd = mul(ways , power)
            toadd = mul(toadd , solve(i - 1 , j - count))
            ans = add(ans , toadd)
    
        dp[i][j] = ans
        return ans
        
    
def answer():
    
        global dp
        dp = [[-1 for i in range(n)] for j in range(k + 1)]
    
        ans = solve(k , n - 1)
    
        return ans
    
    
    
    for T in range(1):
    
        n , k = inp()
    
        
        print(answer())