def run():
        n, k, d = (int(x) for x in input().split(' '))
        value = recurse(n, k, d, 0, dict()) % 1000000007
        print(value)
    
def recurse(n, k, d, r, memo):
        if n == 0:
            if d == -1:
                return 1
            else:
                return 0
        elif n < 0:
            return 0
    
        key = 'level={}, n={}, d={}'.format(r, n, d)
        if key in memo.keys():
            return memo[key]
    
        total = 0
    
        for p in range(1, min(n + 1, k + 1)):
            if p >= d:
                d = -1
    
            value = recurse(n - p, k, d, r + 1, memo)
            total += value
    
        memo[key] = total
    
        return total
    
    run()