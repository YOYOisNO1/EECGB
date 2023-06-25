def program4876():
    
    st = str(input())
    p = ''
    flag = 0
    for index, c in enumerate(reversed(st)):
        if index != len(st)-1:
            if c == '0':
                p += str(9)
                flag = 1
                continue
            elif c == '9':
                p += str(9)
                continue 
            now = int(c)+10-flag-9
            flag = 1 if now != 0 else 0
            p += str(now)
        else:
            p += str(int(c)-flag)
    p = int(p[::-1])
    pp = int(st) - p
    ans = 0
    while p != 0:
        ans += p % 10
        p //= 10
    while pp != 0:
        ans += pp % 10
        pp //= 10
    print(ans)