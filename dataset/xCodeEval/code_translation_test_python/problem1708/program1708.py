def program1708():
    n,m,a,b = map(int,input().split())
    if m == 1:
        print(1)
        exit(0)
    if b == n:
        b = (b+m-1)/m*m
    l = (a+m-1)/m*m
    r = (b+m-1)/m*m
    if r == l:
        print(1)
        exit(0)
    if r == l+m:
        if a % m == 1 and b % m == 0:
            print(1)
        else:
            print(2)
        exit(0)
    d1 = (l-a+1) % m
    d2 = (b-r) % m
    if a % m == 1 and b % m == 0:
        print(1)
        exit(0)
    if a % m == 1 or b % m == 0:
        print(2)
        exit(0)
    if d1 + d2 == m:
        print(2)
        exit(0)
    print(3)
    