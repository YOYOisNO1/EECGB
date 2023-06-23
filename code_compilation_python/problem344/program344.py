def program344():
    s = input()
    ans = ''
    p = len(s) // 2
    for i in range(len(s)):
        if i % 2 != 0:
            ans += s[p + i // 2 + 1]
        else:
            ans += s[p - i // 2]
    a = list(ans)
    print(*a, sep='')