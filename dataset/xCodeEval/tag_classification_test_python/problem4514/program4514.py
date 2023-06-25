def program4514():
    import sys
     
    n = int(sys.stdin.readline())
    d = sys.stdin.readline()
    s = sorted(list(set([int(x) for x in d.split(' ')])))
     
    ans = 0
    while len(s) > 0:
        ans += 1
        ss = []
        for x in s[1:]:
            if x % s[0]:
                ss.append(x)
        s = ss
    print(ans)