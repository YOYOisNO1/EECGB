def program1590():
    n, M = map(int, input().split(' '))
    
    D = [[] for _ in range(n + 1)]
    for d in range(2, n + 1):
        for dst in range(2*d, n + 1, d):
            D[dst].append(d)
    
    
    F = [None] * (n + 1)
    F[1] = 1
    F[2] = 2
    for x in range(3, n + 1):
        F[x] = (2 * F[x - 1] + F[x//(x - 1)]) % M
        S = 0
        for d in D[x]:
            if 2 <= d <= x - 2:
                S += F[x//d] - F[(x - 1)//d]
        F[x] = (F[x] + S) % M
    
    print(F[n] % M)