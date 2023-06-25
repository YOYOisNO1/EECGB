def program2705():
    n = input()
    N = n * (n + 1) / 2
    
    segs = dict()
    for i in range(1, n + 1):
        segs[i] = []
    
    for len in range(1, n + 1):
        for i in range(n, len - 1, -1):
            segs[i].append(len)
    
    lays = 0
    cnt = 0
    curr = n
    while cnt < N:
        while segs[curr] != []:
            cc = curr
            while cc > 0:
                while cc > 0 and segs[cc] == []:
                    cc -= 1
                if cc == 0:
                    break
    
                cct = cc - segs[cc][-1]
                # print((cct,) cc),
                segs[cc].pop()
                cc = cct
                cnt += 1
            lays += 1
            # print("")
        curr -= 1
    
    print(lays)