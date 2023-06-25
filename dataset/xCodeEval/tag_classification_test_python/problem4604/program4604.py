def program4604():
    n, k = map(int, input().split())
    s = input()
    d = {}
    ans = True
    
    for i in set(s):
        d[i] = s.rfind(i)
    cur = set()
    for i in range(n):
        if s[i] in cur:
            if d[s[i]] == i:
                cur.remove(s[i])
        else:
            cur.add(s[i])
            if len(cur) > k:
                ans = False
                break
            if d[s[i]] == i:
                cur.remove(s[i])
    if ans:
        print("NO")
    else:
        print("YES")