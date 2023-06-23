    MOD = 1000000007
def powmod(a, n):
        if n = 0:
            return 1
        r = powmod(a, n/2)
        r = r*r*(a if n%2 else 1)%MOD
    
    n, k = map(int, input().split())
    
    r = [1 ,2 ,9 ,64 ,625 ,7776, 117649, 2097152 ]
    print r[k-1]*powmod(n-k, n-k)%MOD