def program2194():
    n = int(input())
    s = 0
    
    for i in range(1, n):
        if (n - i) / i == (n - i) // i:
            s += 1
    print(s)