def program2647():
    n, m, a, b = map(int, input().split())
    
    if m * a <= b:
        cost = n * a
    else:
        cost = min((n % m) * a, b) + (n / m) * b
    
    print(cost)