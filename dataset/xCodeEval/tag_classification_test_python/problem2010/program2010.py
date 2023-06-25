    memo = {}
    
    tg,k,d = map(int,input().split())
    
def rec(n):
        if n in memo:
            return memo[n]
    
        ans = [0,0]
    
        for b in range(1, min(k,n)+1):
            
            if b == n:
                ans[b>=d]+=1
                continue
    
            r = rec(n-b)
            ans[1]+=r[1]
            ans[b>=d]+=r[0]
    
        memo[n] = ans
        return ans
    
    print(rec(tg)[1]%(10**9+7))