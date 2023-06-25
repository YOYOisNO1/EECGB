def program1640():
    a1 = int(input())
    a2 = int(input())
    k1 = int(input())
    k2 = int(input())
    n = int(input())
    
    minPlayer = (k1-1)*a1 + (k2-1)*a2
    if minPlayer >= n:
        minPlayer = 0
    else:
        minPlayer = n - minPlayer
        if minPlayer > a1+a2:
            minPlayer = a1+a2
    
    l = sorted([[k1, a1], [k2, a2]])
    maxPlayer = 0
    while n >= 0:
        if l[0][1] == 0 and l[1][1] == 0:
            maxPlayer += 1
            break
        elif l[0][1] > 0:
            n -= l[0][0]
            l[0][1] -= 1
            maxPlayer += 1
        elif l[1][1] > 0:
            n -= l[1][0]
            l[1][1] -= 1
            maxPlayer += 1
    print(minPlayer, maxPlayer-1)
    
    
    