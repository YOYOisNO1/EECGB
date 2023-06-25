def program826():
    s = input()
    alph = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if len(s) >= 26:
        ans = -1
        l = 0
        r = 25
        if '?' not in s:
            while ans != 'yes' and r < len(s):
                if set(s[l:r + 1]) == alph:
                    ans = 'yes'
                l += 1
                r += 1
            if ans == 'yes':
                print(s)
            else:
                print(-1)
        else:
            while ans != 'yes' and r < len(s):
                if len(set(s[l:r + 1])) - 1 + s[l:r + 1].count('?') == 26:
                    ans = 'yes'
                    a = set(s[l:r + 1])
                    dif = alph - a
                    dif = list(dif)
                    s = list(s)
                    for i in range(l, r + 1):
                        if s[i] == '?':
                            s[i] = dif.pop()
                    for i in range(len(s)):
                        if s[i] == '?':
                            s[i] = 'A'
                l += 1
                r += 1
            if ans == 'yes':
                for item in s:
                    print(item, end='')
            else:
                print(-1)
    else:
        print(-1)