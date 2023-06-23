    from math import pow
    
    # modular inverse for positive a and b and nCk mod MOD depending on modinv
    
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
    
    
    MOD = 998244353
    
    n, m = map(int, input().split())
    
    mul = n * modinv(m + 1,MOD) + 1
    
    mul %= MOD
    
    curN = 1
    
    for i in range(1,n + 1):
        curN += m * pow(i, -1, MOD)
        curN %= MOD
    
    curN *= mul
    
    curN %= MOD
    
    print(curN)
    