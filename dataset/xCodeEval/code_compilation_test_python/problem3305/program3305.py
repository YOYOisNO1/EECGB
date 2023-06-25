    MOD = 10 ** 9 + 7
    
def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    
def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
    
def combination(n,k,MOD): 
        ans = 1
        for i in range(n - k + 1, n + 1):
            ans *= i
            ans %= MOD
        for i in range(k):
            ans *= modinv(i,MOD)
            ans %= MOD
        return ans
    
    n,m,k = map(int,input().split())
    
    print(combination(n-1,n-2 * k-1) * combination(n-1,n - 2 * k - 1) % MOD)
    