def program4837():
    n = int(input())
    M = []
    s = 0
    for i in range(n): M.append([int(x) for x in input().split()])
    for x in range(n):
        for y in range(n):
            if x == y or x+y == n-1 or x == (n-1)//2 or y == (n-1)//2: s += M[x][y]
    print(s)