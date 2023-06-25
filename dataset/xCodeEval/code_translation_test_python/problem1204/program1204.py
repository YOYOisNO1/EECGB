def program1204():
    (n, k, x) = map(int, input().split())
    bolas = map(int, input().split())
    ans = 0
    
    for i in range(n):
        s = bolas[:]
        s.insert(i, x)
        while len(s) > 2:
            l = len(s)
            for j in range(2, len(s)):
                if s[j-2] == s[j-1] == s[j]:
                    p = j + 1
                    while p < len(s):
                        if s[j] != s[p]:
                            break
                        p += 1
                    s = s[:j-2] + s[p:]
                    break
            if len(s) == l:
                break
        ans = max(ans, n - len(s))
    
    print(ans)