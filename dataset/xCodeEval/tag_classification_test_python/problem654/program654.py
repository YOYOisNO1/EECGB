def program654():
    n, m = map(int, input().split())
    
    minA = max(0, n - 2*m)
    
    curC = 0
    
    curE = 0
    curMax = curC * (curC - 1) // 2
    while m > 0:
        if m > curMax - curE:
            m -= curMax - curE
            curE = curMax
            curC += 1
            curMax = curC * (curC - 1) // 2
        elif m == curMax - curE:
            break
        else:
            break
    maxA = n - curC
    
    print(str(minA) + ' ' + str(maxA))