    rr=input
    rrI = lambda: int(rr())
    rrM = lambda: map(int,rr().split())
    debug=0
    if debug:
        fi = open('t.txt','r')
        rr=lambda: fi.readline().replace('\n','')
    
def good_mask(x):
        if x == 0: return False
        return (x+1) & x == 0
    
    N = rrI()
    S = rr()
    MOD = 10**9 + 7
    UPPER = 22
    
    
    memo = {}
def dp(i, mask):
        #Having made a cut already before position i,
        #and having a set of mask taken
        #how many ways?
        if i == N:
            return 1 if good_mask(mask) else 0
        if (i,mask) in memo:
            return memo[i,mask]
        ans = 1 if good_mask(mask) else 0
        for j in xrange(i+1, N+1):
            num = int(S[i:j], 2)
            if num == 0: continue
            if num >= UPPER: break
            ans += dp(j, mask | (1<<(num-1)))
            if ans >= MOD:
                ans %= MOD
        memo[i, mask] = ans
        return ans
    
    fans = 0
    for i in xrange(N):
        fans += dp(i, 0)
        if fans >= MOD:
            fans %= MOD
    print fans