def program3124():
    n = int(input())
    s = input() + '0'
    ans = 0
    i = 0
    while i < n:
        ctr = 0
        while i != '0':
            ctr += 1
            i += 1
        i += 1
        ans *= 10
        ans += ctr
    print(ans)
        