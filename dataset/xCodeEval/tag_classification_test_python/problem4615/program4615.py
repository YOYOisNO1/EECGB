def program4615():
    from collections import deque
    n, k = list(map(int, input().split()))
    s = input()
    rs = s[::-1]
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last = {}
    for c in alpha:
        p = rs.find(c)
        if p != -1:
            last.update({c: n - p - 1})
    amount = 0
    o = deque()
    c = 0
    for i in range(len(s)):
        if s[i] not in o:
            o.append(s[i])
            c += 1
        if c > k:
            print('YES')
            break
        if i == last[s[i]]:
            c -= 1
    else:
        print('NO')