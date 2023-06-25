    from bisect import bisect_left as bis
def process(l,m):
        nn = len(l)
        mods = []
        for i in range(pow(2,nn)):
            s = bin(i)[2:].zfill(len(l))
            mods.append(sum([l[i] for i in range(nn) if s[i] == '1'])%m)
        return mods
    
    
    n,m = map(int, input().split())
    l = map(int, input().split())
    l1 = l[:n/2]
    l2 = l[n/2:]
    ll1, ll2 = process(l1,m), process(l2,m)
    ll1.sort()
    ans = max(ll1)
    for i in ll2:
        kk = m-i
        temp = bis(ll1,kk)
        if temp >= len(ll1):
            ans = max(ans, (ll1[-1]+i)%m)
        elif temp == 0:
            ans = max(ans,i)
        else:
            ans = max(ans,(ll1[temp-1]+i)%m)
    print(ans)