    N, mod = map(int, input().split())
    NNN = (10**5)
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]
def mul(a, b):
        return ((a % mod) * (b % mod)) % mod
    
    for i in range( 2, NNN + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
    
    r = 0
    for i in range(1, N+1):
        r += mul(mul(mul((N-i+1),(N-i+1)),g1[N-i]),g1[i])
        r %= mod
    print(r)