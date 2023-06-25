    maximal = 1000000007
def binpow (a, n):
        if n==0:
            return 1
        if n%2 == 1:
            return (binpow(a, n-1) * a) % maximal
        else:
            b = binpow(a, int(n/2)) % maximal
            return (b*b) % maximal
    n, m = map(int, input().split())
    sf = (binpow(2, m) - 1 + maximal) % maximal
    rez = binpow(sf, n) % maximal
    print(str(int(rez)))