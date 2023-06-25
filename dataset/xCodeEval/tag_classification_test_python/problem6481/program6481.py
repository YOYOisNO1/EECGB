def program6481():
    from sys import stdin
    
    kDic = {c: i for i, c in enumerate("RGBYW12345")}
    
    ibuf = stdin.readlines()
    s = list(set(ibuf[1].split()))
    t = []
    
    for i in xrange(len(s)):
        for j in xrange(i + 1, len(s)):
            t.append([0, 0])
            if s[i][0] != s[j][0]:
                t[-1][0] = (1 << kDic[s[i][0]]) | (1 << kDic[s[j][0]])
            if s[i][1] != s[j][1]:
                t[-1][1] = (1 << kDic[s[i][1]]) | (1 << kDic[s[j][1]])
    
    res = 10
    for i in xrange(2 ** 10 - 1):
        b = [(x & i) | (y & i) for x, y in t]
        if 0 not in b:
            res = min(res, bin(i).count("1"))
    print(res)