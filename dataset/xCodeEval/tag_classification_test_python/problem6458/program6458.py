def program6458():
    from sys import stdin
    
    kDic = {c: i for i, c in enumerate("RGBYW12345")}
    
    ibuf = stdin.readlines()
    s = list(set(ibuf[1].split()))
    t = []
    
    for i in xrange(len(s)):
        for j in xrange(i + 1, len(s)):
            t.append(((1 << kDic[s[i][0]]) ^ (1 << kDic[s[j][0]])) | ((1 << kDic[s[i][1]]) ^ (1 << kDic[s[j][1]])))
    
    res = 10
    for i in xrange(2 ** 10 - 1):
        b = [x & i for x in t]
        if 0 not in b:
            res = min(res, bin(i).count("1"))
    print(res)