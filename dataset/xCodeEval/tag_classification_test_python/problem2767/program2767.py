def program2767():
    s = input()
    
    k = 0
    flag = True
    t = set()
    for x in range(len(s) // 2 + 1):
        if s[x] != s[-(x + 1)]:
            flag = False
            break
        t.add(s[x])
    
    if not flag:
        print(len(s))
    elif len(t) == 1:
        print(0)
    else:
        print(len(s) - 1)
    