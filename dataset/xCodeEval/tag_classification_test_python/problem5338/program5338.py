    class BIT:
    def __init__(self,n:int):
            q = 1 << (n - 1).bit_length() + 1
            self.ceiling = q
            self.bittree = [0]*(q + 1)
    
    def updatebit(self, v:int, n:int):
            v = v * 2 - 1
            self.bittree[v] = n
            while v < self.ceiling:
                s = int(v)
                count = 0
                while not s & 1:
                    s >>= 1
                    count += 1
                v += 2 ** count
                self.bittree[v] += n
        
    def getIntervalSum(self,l:int,r:int):
            #[l,r]
            l = l * 2 - 2
            r = r * 2 - 1
            ret = 0
            while r > 0:
                ret += self.bittree[r]
                s = int(r)
                count = 0
                while not s & 1:
                    s >>= 1
                    count += 1
                r -= 2 ** count
            while l > 0:
                ret -= self.bittree[l]
                s = int(l)
                count = 0
                while not s & 1:
                    s >>= 1
                    count += 1
                l -= 2 ** count
            return ret
    
    
    
    n, mod = map(int,input().split())
    
    dp = [0 for _ in range(n + 1)]
    
    bittree = BIT(n)
    
    dp[n] = 1
    bittree.updatebit(n,1)
    sum = 1
    
    
    for i in range(n-1,0,-1):
        for j in range(2,n+1):
            if i * j <= n:
                dp[i] = (dp[i] + bittree.getIntervalSum(i*j,min((i+1)*j - 1,n))) % mod
            else:
                break
        dp[i] = (dp[i] + sum) % mod
        bittree.updatebit(i,dp[i])
        sum = (sum + dp[i]) % mod
    print(dp[1])