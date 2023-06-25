    DIMZ = 50
    MOD = 10**9+7
    
def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    
def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            0/0
        else:
            return x % m
    
def matmul(a,b, DIM=DIMZ):
        res = [[0 for i in range(DIM)] for j in range(DIM)]
        for i in range(DIM):
            for j in range(DIM):
                for k in range(DIM):
                    res[i][j] += a[i][k] * b[k][j]
                res[i][j] %= MOD
        return res
    
def matpow(mat, n):
        if n==1: return mat
        if n%2: return matmul(mat, matpow(matmul(mat, mat), n/2))
        return matpow(matmul(mat, mat), n/2)
            
def divisors(n):
        factors = {}
        nn = n
        i = 2
        while i*i <= nn:
            while nn % i == 0:
                if not i in factors:
                    factors[i] = 0
                factors[i] += 1
                nn //= i
            i += 1
        if nn > 1:
            factors[nn] = 1
        return factors
    
    n,k = map(int, input().split())
    
    mat = [[0 for c in range(DIMZ)] for l in range(DIMZ)]
    
    for c in range(DIMZ):
        coef = modinv(DIMZ-c, MOD)
        for l in range(DIMZ-c):
            mat[-1-l][c] = coef
    
    mp = matpow(mat, k)
    
    factors = divisors(n)
    
    tot = 1
    for fact in factors:
        nf = factors[fact]
        myexp = 0
        for i in range(DIMZ):
            myexp += pow(fact,DIMZ-i-1)*mp[i][DIMZ-nf-1]
            #print(fact,) i, pow(fact,DIMZ-i-1)*mp[i][DIMZ-nf-1]
        tot *= myexp
        tot %= MOD
    
    print(tot%MOD)
    