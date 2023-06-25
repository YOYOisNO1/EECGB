def program4005():
    w, m = map(int, input().split())
    while m > 0:
        digit = m % w
        if digit == 1:
            m -= 1
        elif digit == w - 1:
            m += 1
        elif digit != 0:
            m = -1
        if m > 0:
            m //= w
    print("YES" if m == 0 else "NO")