def program5626():
    
    n, m = map(int ,input().split(' '))
    if n == 1:
        print(m)
    elif m == 1:
        print(n)
    else:
        if n == 2 or m == 2:
            if m == 2:
                t = m
                m = n
                n = t
            ans = m / 4 * 4
            if m % 4 >= 2:
                ans += 4
            elif m % 4 == 1:
                ans += 2
            print(ans)
        else:
            print((n) * m + 1) / 2