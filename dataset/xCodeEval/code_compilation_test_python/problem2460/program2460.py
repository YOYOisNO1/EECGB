    n, m = [int(x) for x in input().split()]
    
def f(n):
        product = 1
        for t in range(1, n + 1):
            product *= t
        return product
    
    num = 1
    for t in range(num):
        num = ((m - m // f(t)) % 998244353 * num) % 998244353
    return num
        