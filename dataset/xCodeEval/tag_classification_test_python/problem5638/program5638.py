def program5638():
    # r102 - D div2
    n, m = map(int, input().split())
    if n > m: n,m = m,n
    
    if n == 1: print(m)
    elif n == 2: print((m/4)*4) + min(2,(m%4))*2
    elif (n*m) % 2 == 0: print((n*m)/2)
    else: print((n*m)/2) + 1