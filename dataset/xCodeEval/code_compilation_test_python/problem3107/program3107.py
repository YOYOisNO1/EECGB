    dp = {(0, 0) : 1}
def f(n, h):
        #print n, h
        if (n, h) in dp:
            return dp[(n, h)]
    
        if n == 0 or h == 0:
            return 0
    
        ans = 0
        for i in xrange(n): #0 .. n-1
            for j in xrange(h): #0 .. h-1
                #print n, n-i-1, i
                ans += f(n-i-1, j) * f(i, h-1)
                ans += f(n-i-1, h-1) * f(i, j)
            ans -= f(n-i-1, h-1) * f(i, h-1)
    
        #print n, h, ans
        dp[(n, h)] = ans
        return ans
    
    n, h = map(int, input().split())
    print sum([ f(n, i) for i in xrange(h, n+1)])