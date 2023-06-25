def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
def nok(a, b):
        return a * b // gcd(a, b)
    
def prime(a):
        i = 2
        while i * i <= a and a % i != 0:
            i += 1
        return i * i > a
    
    n, m = map(int, input().split())
    mod = 998244353
    res = 0
    ans = 1
    div = 1
    for i in range(1, n + 1):
        if prime(i):
            div *= i
        ans *= m // div
        res += pow(m, i, mod) - ans % mod
    print(res % mod)