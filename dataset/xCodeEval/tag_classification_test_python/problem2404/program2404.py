def program2404():
    n = int(input())
    s = input()
    ans1 = ans2 = 0
    cur = now = 0
    for i in s:
        if i == '(':
            ans1 = max(ans1, cur)
            cur = 0
            now = 1
        elif i == ')':
            if cur: ans2 += 1
            cur = 0
            now = 0
        elif i == '_':
            if now == 0: ans1 = max(ans1, cur)
            elif cur: ans2 += 1
            cur = 0
        else:
            cur += 1
            if now == 0: ans1 = max(ans1, cur)
    print(ans1, ans2)