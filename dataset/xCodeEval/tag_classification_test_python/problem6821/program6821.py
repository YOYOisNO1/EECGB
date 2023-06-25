def program6821():
    k = int(input())
    s = list(input())
    n = len(s)
    a = [0] * 26
    p = 0
    q = 0
    fin = n // 2
    start = n // 2 - 1
    if n % 2 == 1:
        fin = (n + 1) // 2
        start += 1
    for i in range(fin):
        if s[i] == '?'and s[n - 1 - i] == '?':
            q += 1
        elif s[i] != '?' and s[n - 1 - i] == '?':
            s[n - 1 - i] = s[i]
            if not a[ord(s[i]) - 97]:
                a[ord(s[i]) - 97] = 1
                p += 1
        elif s[n - 1 - i] != '?' and s[i] == '?':
            s[i] = s[n - 1 - i]
            if not a[ord(s[i]) - 97]:
                a[ord(s[i]) - 97] = 1
                p += 1
        else:
            if s[i] != s[n - 1 - i]:
                print('IMPOSSIBLE')
                exit()
            if not a[ord(s[i]) - 97]:
                a[ord(s[i]) - 97] = 1
                p += 1
    if q < k - p:
        print('IMPOSSIBLE')
        exit()
    for i in range(start, -1, -1):
        if s[i] == '?' and s[n - 1 - i] == '?':
            if p < k:
                for j in range(k - 1, -1, -1):
                    if not a[j]:
                        s[i] = chr(97 + j)
                        s[n - 1 - i] = chr(97 + j)
                        p += 1
                        a[j] = 1
                        break
            else:
                s[i] = 'a'
                s[n - 1 - i] = 'a'
            q -= 1
    print(''.join(s))