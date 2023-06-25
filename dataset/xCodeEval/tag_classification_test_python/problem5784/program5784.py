    import sys
    input = sys.stdin.readline
    
    n = int(input())
    s = input()
    dp = [[-1]*n for i in range(n)]
    
def f(l, r):
        if l > r:   return 0
        if l == r:  return 1
        if dp[l][r] != -1:  return dp[l][r]
        
        '''
        f(l, r) = min number of steps to delete s[l...r]
        We can have two ways:
            - Delete s[l] only -> f(l, r) = 1 + f(l+1, r)
            - Delete s[l] with some char s[i] (l+1 <= i <= r) and s[i] == s[l]
                - To be able to delete s[l] and s[i] in a single step, we must
                  first optimally delete s[l+1...i-1]
                -> f(l, r) = f(l+1, i-1) + f(i, r)
                - As there can be many valid s[i]s, we choose the one which gives
                  the minimum cost
        ''' 
    
        best = 1 + f(l+1, r)
        for i in range(l+1, r+1):
            if s[i] == s[l]:
                current = f(l+1, i-1) + f(i, r)
                best = min(best, current)
        dp[l][r] = best
        return best
    
    print(f(0, n-1))