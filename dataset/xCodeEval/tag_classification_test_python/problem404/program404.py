def dyn_ribbons(n, r):
    
        memo = {}
    
    def ribbons(m):
    
            if m in memo.keys():
                return memo[m]
    
            elif m < 0:
                return - 1
    
            elif m == 0:
                return 0
    
            elif 0 < m < min(r):
                return -1
    
            elif m == min(r):
                return 1
    
            else:
                memo[m] = max([-1] + [1 + ribbons(m - s) for s in r if ribbons(m - s) >= 0])
                return memo[m]
    
    
        for i in range(n):
            ribbons(i)
    
        return ribbons(n)
    
    
    n, a, b, c = [int(x) for x in input().split(' ')]
    r = [a, b, c]
    r = [s for s in r if s <= n]
    
    print(dyn_ribbons(n, r))