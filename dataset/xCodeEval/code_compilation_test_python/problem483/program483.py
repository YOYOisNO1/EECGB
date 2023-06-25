def program483():
    n, a, b = map(int, input().split())
    c = [int(x) for x in input().split()]
    if a < b:
        min = a
    else:
        min = b
    if n % 2 == 0:
        middle = n // 2 + 1
        s = 0
    else:
        middle = n // 2
        s = min if c[middle] == 2
    
    for i in range(middle):
        if c[i] == c[n - i - 1] and c[i] != 2:
            continue
        else:
            if (c[i] == 1 and c[n - i - 1] == 0) or (c[i] == 0 and c[n - i - 1] == 1):
                s = -1
                break
            elif (c[i] == 1 and c[n - i - 1] == 2) or (c[i] == 2 and c[n - i - 1] == 1):
                s += b
            elif (c[i] == 0 and c[n - i - 1] == 2) or (c[i] == 2 and c[n - i - 1] == 0):
                s += a
            elif c[i] == 2 and c[n - i - 1] == 2:
                s += 2 * min
    
    print(s)