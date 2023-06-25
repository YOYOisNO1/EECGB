    fac = [1]
    for i in range(1,16):
        fac.append(i*fac[-1])
    DP = {(0,0,0,0):1,(0,0,0,1):1,(0,0,0,2):1,(0,0,0,3):1}
def combs(a,b,c,d):
        hs = (a,b,c,d)
        if hs in DP: return DP[hs]
        if min(a,b,c) < 0:
            DP[hs] = 0
            return 0
        DP[hs] = 0
        if d != 0: DP[hs] += combs(a-1,b,c,0)
        if d != 1: DP[hs] += combs(a,b-1,c,1)
        if d != 2: DP[hs] += combs(a,b,c-1,2)
        return DP[hs]
def s(i):
        sm = 0
        for j in range(N):
            if i & (1<<j): sm += songs[j][0]
        return sm == T
def calc(i):
        a = [0,0,0]
        for j in range(N):
            if i & (1<<j): a[songs[j][1]-1] += 1
        return fac[a[0]]*fac[a[1]]*fac[a[2]]*combs(a[0],a[1],a[2],3)
    N,T  = map(int,input().split())
    songs = [tuple(map(int,input().split())) for _ in range(N)]
    out = 0
    for i in range(2**N):
        if s(i):
            out += calc(i)
    print((out%(10**9+7)))