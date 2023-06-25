    N = 200001
    MOD = 1000000007
    fact = [1] * N
    inv_fact = [1] * N
    
def ModExp(a, n):
        ans = 1
        while n:
            if n % 2:
                ans = (ans * a) % MOD
            a = (a * a) % MOD
            n /= 2
        return ans
    
def ModInverse(a):
        return ModExp(a, MOD - 2)
    
def PreProcess(n):
        for i in range(1, n + 1):
            fact[i] = (i * fact[i - 1]) % MOD
    
        inv_fact[n] = ModInverse(fact[n])
        for i in range(n - 1, 0, -1):
            inv_fact[i] = ((i + 1) * inv_fact[i + 1]) % MOD
    
def nCr(n, r):
        if n < 0 or r < 0 or n < r:
            return 0
        else:
            return (fact[n] * (inv_fact[r] * inv_fact[n - r]) % MOD) % MOD
    
def Beggar(m, n):
        if m < 0 or n < 0 or (n == 0 and m != 0):
            return 0
        else:
            if m + n == 0:
                return 1
            else:
                return nCr(m + n - 1, m)
    
    f, w, h = map(int, input().split())
    n = f + w
    
    PreProcess(n)
    
    q = nCr(n, w)
    p = 0
    
    for n in range(0, w + 1):
        if n * (h + 1) > w:
            break
        else:
            p += (Beggar(w - n * (h + 1), n) * ((Beggar(f - n - 1, n + 1) + Beggar(f - n + 1, n - 1) + 2 * Beggar(f - n, n)) % MOD)) % MOD
    
    q = ModInverse(q)
    ans = (p * q) % MOD
    
    print ans