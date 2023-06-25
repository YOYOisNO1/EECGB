def program682():
    #!/usr/bin/env python3
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * 100
    c = [0] * n
    
    for x in range(n):
        for y in range(a[x]):
            b[y] += 1
    
    for x in range(100):
        for y in range(b[x]):
            c[n-y-1] += 1
    
    for x in range(n):
        print(c[x], end=" ")