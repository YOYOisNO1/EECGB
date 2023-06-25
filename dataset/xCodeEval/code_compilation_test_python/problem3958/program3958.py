    fac = [1]
    for i in range(1,16):
        fac.append(i*fac[-1])
    DP = {(0,0,0):1}
def combs(a,b,c):
        x,z = min(a,b,c),max(a,b,c)
        y = a+b+c-x-z
        hs = (x,y,z)
        if x+y+1<z or x < 0:
            DP[hs] = 0
            return 0
        if hs in DP: return DP[hs]
        DP[hs] = combs(x-1,y,z)+combs(x,y-1,z)+combs(x,y,z-1)
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
        return fac[a[0]]*fac[a[1]]*fac[a[2]]*combs(a[0],a[1],a[2])
    N,T  = map(int,input().split())
    songs = [tuple(map(int,input().split())) for _ in range(N)]
    out = 0
    for i in range(2**N):
        if s(i):
            out += calc(i)
    print (out%(10**9+7))