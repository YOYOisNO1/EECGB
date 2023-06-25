    n, m, t = map(int, input().split())
    fact = [1] * 100
    
    for i in range(1, 100):
        fact[i] = fact[i - 1] * i
    
    
def nck(n, k):
        return fact[n] // (fact[n - k] * fact[k])
    
    
    total = 0
    for i in range(4, t):
        total += nck(n, i) * nck(m, t - i)
    print(total)