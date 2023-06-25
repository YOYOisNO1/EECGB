def program1800():
    n = int(input()); L = [int(x) for x in input().split()]
    p = len([x for i, x in enumerate(L) if x > 0])
    m = len([x for i, x in enumerate(L) if x < 0])
    if p >= (n+1)//2: print(1)
    elif m >= (n+1)//2: print(-1)
    else print(0)