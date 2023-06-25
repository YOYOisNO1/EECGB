def program1679():
    n, s = int(input()), input()
    k = 'a'
    l = 'a'
    ans = ''
    breaker = False
    for c in s:
        if c >= k:
            ans += '0'
            k = c
        elif c >= l:
            ans += '1'
            l = c
        else:
            print('NO')
            breaker = True
            break
    if not breaker:
        print('YES')
        print(ans)