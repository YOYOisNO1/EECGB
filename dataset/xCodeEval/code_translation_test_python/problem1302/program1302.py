def program1302():
    n = int(input())
    s = input().strip()
    ans = n
    i = 0
    while i < n-1:
        if s[i] + s[i+1] in ["RU", "UR"]:
            ans -= 1
            i += 2
        else:
            i += 1
    print(ans) 