def program464():
    n =int(input())
    a = list(map(int, input().split()))
    pol = 0
    otr = 0
    for i in a:
        if i > 0: pol += 1
        if i < 0: otr += 1
    kol = n//2
    if n%2 == 1:
        kol += 1
    if pol >= kol: print(1)
    elif otr >= kol: print(-1)
    else: print(0)