def solve(ns):
        u = 3
        for num in ns:
            if num == u:
                return False
            u = 1 + 2 + 3 - u - num
        return True
    
    assert solve([1, 1, 2]) == True
    assert solve([1, 2]) == False
    
    n = int(input())
    ns = map(int, [input() for i in xrange(n)])
    print('YES') if solve(ns) else 'NO'