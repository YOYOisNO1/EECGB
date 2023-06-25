def program3997():
    w, m = map(int, input().split())
    
    cnt = 0
    while m > 1 and cnt < 100:
        if (m - 1) % w == 0:
            m -= 1
        elif m % w == 0:
            m = m
        elif (m + 1) % w == 0:
            m += 1
        else:
            break
        m /= w
        cnt += 1
    
    print('YES') if m == 1 else 'NO'