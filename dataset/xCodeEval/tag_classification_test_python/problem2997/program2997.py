    from sys import stdin
    input = stdin.readline
    
    inp = lambda : list(map(int,input().split()))
    
    mod = 998244353
def add(a , b):return ((a%mod) + (b%mod))%mod
def sub(a , b):return (a - b + mod)%mod
def mul(a , b):return ((a%mod) * (b%mod))%mod
def ncr(n , r):
        if(r > n):return 0
        return mul(fact[n] , mul(facti[n - r] , facti[r]))
def div(a , b):return mul(a , pow(b , mod - 2 , mod))
    
    fact , facti = [1] , [1]
    size = 2 * (10**5) + 1
    for i in range(1 , size):
        fact.append(mul(fact[-1] , i))
        facti.append(pow(fact[-1] , mod - 2 , mod))
    
    c = [[0 for i in range(501)] for j in range(501)]
    for i in range(501):
        for j in range(501):
            c[i][j] = ncr(i , j)
            
    
def solve(i , j):
    
        if(i == 0):return 1
        if(i == 1 or j > x):return 0
        if(dp[i][j] != -1):return dp[i][j]
        
        ans = 0
        for todie in range(i + 1):
    
            ways = c[i][todie]
            this = min(i - 1 , x - j)
            power = pow(this , todie , mod)
            toadd = mul(ways , power)
            toadd = mul(toadd , solve(i - todie , j + i - 1))
    
            ans = add(ans , toadd)
    
        dp[i][j] = ans
        return ans   
        
    
def answer():
    
        global dp
        dp = [[-1 for i in range(x + 1)] for j in range(n + 1)]
    
        ans = solve(n , 0)
        return ans
    
    for T in range(1):
    
        n , x = inp()
    
        
        print(answer())