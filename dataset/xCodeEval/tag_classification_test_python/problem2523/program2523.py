def program2523():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = int(n**0.5 + 10**(-10))
        c = int(n**(1/3) + 10**(-10))
        remove = int(n**(1/6)+10**(-10))
        
        print(s + c - remove)
        