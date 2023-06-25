    
    import sys
    sys.setrecursionlimit(2 ** 20)
    
    n, k, d = map(int, input().split())
    ways = 0
    
    dp = [ [ -1 for y in xrange(2) ] for x in xrange(n+1) ]
    
def getWays(total = 0, got = 0):
        global ways, n, k, d, dp
        
        if total > n :
            return 0
        
        if total == n :
            return got 
        
        if dp[total][got] != -1 :
            return dp[total][got]
            
        dp[total][got] = 0
        
        for i in xrange(1, k+1):
            if i >= d :
                dp[total][got] += getWays(total + i, 1)
            else :
                dp[total][got] += getWays(total + i, got)
                
        return dp[total][got]
    
    print(getWays()) % 1000000007