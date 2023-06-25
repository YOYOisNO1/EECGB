def program4510():
    
    n, m = map(int, input().split())
    
    fact = [1]
    for i in range(1, n + 1):
    	fact.append((fact[-1] * i) % m)
    
    total = 0
    
    for k in range(1, n + 1):
    	total = (total + ((((((n - k + 1) * (n - k + 1)) % m) * (fact[k])) % m) * fact[n - k]) % m) % m
    print(total)