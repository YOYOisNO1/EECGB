def program2736():
    n = input()
    m = input()
    
    sol = []
    
    for i in range(0, n + 1):
        sol.append(0)
    
    for i in range(0, m):
        x = input()
        for j in range(x, n + 1):
            if sol[j] == 0:
                sol[j] = x
    
    print sol[1 : n + 1]
        