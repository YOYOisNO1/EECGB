def program5550():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    g = b-c
    t=0
    if g < a and b <= n:
        t+=(n-b)/(b-c) + 1
        n -= t*g
    if a <= n:
        t+=n/a
    print(t)