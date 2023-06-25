def program4760():
    n, m = map(int, input().rstrip().split(" "))
    n, m = min(n, m), max(n, m)
    if 2*n < m:
        r = n
    else:
        r = (n + m)//3
    print(r)