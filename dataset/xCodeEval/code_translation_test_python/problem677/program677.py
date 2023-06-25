    n, m = map(int, input().split())
    
def modular_expo(n, m):
        if n == 1:
            return 3
        if n == 0:
            return 1
        if n % 2 == 0:
            temp = modular_expo(n/2, m)
            return ((temp % m) * (temp % m)) % m
        else:
            return (3 * (modular_expo(n-1, m) % m)) % m
    
    ans = modular_expo(n, m)
    print((ans-1+m)) % m