def program6462():
    n = int(input())
    t = [i for i in input().split()]
    vis = set()
    save = []
    for s in t:
        if s in vis:
            n -= 1
            continue;
        else:
            save.append(s)
            vis.add(s)
    
    
    res = 20
    ID = {i:c for i,c in enumerate('RGBYW12345') }
    for k in range(1 << 11):
        status = {c:0 for c in 'RGBYW12345'}
        num = {c:0 for c in 'RGBYW12345'}
        cnt = 0
        for i in range(10):
            if k & (1 << i) != 0:
                status[ID[i]] = 1
                cnt += 1
        untwo = 0
        for s in save:
            if status[s[0]] == 0 and status[s[1]] == 0:
                untwo += 1
                continue
            if(status[s[0]] == 0):
                num[s[1]] += 1
            if(status[s[1]] == 0):
                num[s[0]] += 1
        if untwo > 1:
            continue
        ok = 1
        for c in num.values():
            if c > 1:
                ok = 0
                break
        if ok == 0:
            continue
        if cnt < res:
            res = cnt
    print(res)