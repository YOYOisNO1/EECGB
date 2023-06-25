    from fractions import gcd
def f(a, b, n):
        return 1-f(b, a, n-gcd(a, n) if n>=0 else 1
    
    print f(*map(int, input().split()))