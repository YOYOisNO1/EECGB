    import itertools
    n = int(input())
    f = list(map(int,input().split()))
    s = list(map(int,input().split()))
    fc = f[:]
    sc = s[:]
    win = 0
    mWin = 999999999999999
def func(i,g):
        m = min(f[i],s[g])
        f[i]-=m
        s[g]-=m
        return m
    win += func(0,1)
    win += func(1,2)
    win += func(2,0)
    perms = list(itertools.permutations([[0,2],[1,0],[2,1],[0,0],[1,1],[2,2]]))
    for i in range(len(perms)):
        now = 0
        f = fc[:]
        s = sc[:]
        for g in range(6):
            m = min(f[perms[i][g][0]],s[perms[i][g][1]])
            f[perms[i][g][0]]-=m
            s[perms[i][g][1]]-=m
        
        now = min(f[0],s[1]) + min(f[1],s[2]) + min(f[2],s[0])
        mWin = min(mWin,now)
    
    print(mWin,win)