def recul(s, dex, cntBig, cntSame) :
        global n, L
        if cntBig > 1 : return 0.0
        if dex == n :
            if cntBig > 1 : return 0.0
            elif cntBig == 1 :
                if cntSame == 0 : return 0.0
                else : return 1.0
            else :
                if cntSame < 2 : return 0.0
                else : return 1.0
                
        ret = 0.0
        P = [0,0,0]
        total = L[dex][1]-L[dex][0]+1
        P[0] = min(max((s - L[dex][0]) / total, 0.0), 1.0)
        P[1] = 0 if s < L[dex][0] or s > L[dex][1] else 1.0/total
        P[2] = min(max((L[dex][1] - s) / total, 0.0), 1.0)
        ret += recul(s, dex+1, cntBig+1, cntSame) * P[2]
        ret += recul(s, dex+1, cntBig, cntSame+1) * P[1]
        ret += recul(s, dex+1, cntBig, cntSame) * P[0]
        return ret
    
    n = int(input())
    L = []
    for i in range(n) :
        l,r = map(int, input().split(' '))
        L.append([l,r])
    ans = 0.0
    S = [0]*10001
    for s in range(1, 10001) :
        S[s] = recul(s, 0, 0, 0)
    for s in range(1, 10001) :
        ans += s*S[s]
    print('{0:.10f}'.format(ans))