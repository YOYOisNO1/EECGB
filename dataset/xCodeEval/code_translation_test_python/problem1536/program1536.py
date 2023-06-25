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
    #N = 75
    #from time import time
    #S  = '100000111111101000100001011100010111110011111011100011001111101111100011110'
    #tt = time()
    #print(tt)
    
    lenbin = [ len(bin(n)) - 2 for n in xrange(32) ]
    
def solve():
        MOD = 10**9 + 7
        number = [ [0]*(N+1) for _ in xrange(N) ]
        for i in xrange(N):
            for j in xrange(i+1, N+1):
                number[i][j] = min(22, int(S[i:j],2))
        #UPPER = 22
        UPPER = 22
        memo = [ {} for _ in xrange(N+1)]
    def dp(i, mask, sum_to_make = 0, cur_max = 0):
            #Having made a cut already before position i,
            #and having a set of mask taken
            #how many ways?
            if i == N:
                return 1 if sum_to_make == 0 != mask else 0
            if mask in memo[i]: return memo[i][mask]
            ans = 1 if sum_to_make == 0 != mask else 0 #good_mask(mask) else 0
            for j in xrange(i+1, N+1):
                num = number[i][j]
                if num == 0: continue
                if num >= UPPER: break
                if sum_to_make > N-j+5: break
                if (mask >> (num-1))&1:
                    ans += dp(j, mask, sum_to_make, cur_max)
                elif num <= cur_max:
                    ans += dp(j, mask|(1<<(num-1)), sum_to_make - lenbin[num], cur_max)
                else:
                    ans += dp(j, mask|(1<<(num-1)), sum_to_make + sum(lenbin[x] for x in xrange(cur_max + 1, num)), num)
                        
                if ans >= MOD:
                    ans %= MOD
            memo[i][mask] = ans
            return ans
        fans = i = 0
        while i < N:
            fans += dp(i, 0)
            fans %= MOD
            i += 1
        
        print(fans)
    #print(time()-tt)
    
    if __name__ == "__main__": solve()
    
    """
def good_mask(x):
        if x == 0: return False
        return (x+1) & x == 0
    
    N = rrI()
    S = rr()
    ##print('.')
    #N = 75
    #import random
    #S = "".join(str(random.randint(0,1)) for _ in xrange(N))
    MOD = 10**9 + 7
    UPPER = 22
    
    memoslide = {N : 0, N-1:0}
def slide(j):
        if j in memoslide:
            return memoslide[j]
        if S[j] == '1':
            memoslide[j] = 0
            return 0
        else:
            k = j
            while k < len(S) and S[k] == '0':
                k += 1
            memoslide[j] = k - j
            return k - j
        
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
            if num > 8:
                #prune
                newmask = mask
                ii = excess = 0
                while newmask:
                    if newmask%2 == 0:
                        excess += len(bin(ii)) - 2
                    ii += 1
                    newmask /= 2
                if excess > N-j+1:
                    break
            k = slide(j)
            newmask = mask | (1<<(num-1))
            bns = dp(j + k, newmask)
            for kk in xrange(k):
                memo[(j + kk, newmask)] = bns
            ans += (1+k) * bns
    
            if ans >= MOD:
                ans %= MOD
        memo[i, mask] = ans
        return ans
    
    fans = 0
    for i in xrange(N):
        fans += dp(i, 0)
        if fans >= MOD:
            fans %= MOD
    print(fans)
    """